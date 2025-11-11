from __future__ import annotations

import re
from dataclasses import dataclass, field, replace
from typing import (
    Any,
    Dict,
    Iterable,
    Match,
    Pattern,
    Sequence,
    Union,
    cast,
)

from maxo import Bot
from maxo.routing.filters import BaseFilter
from maxo.routing.updates import MessageCreated
from maxo.types.bot_command import BotCommand
from maxo.utils.payload import decode_payload

CommandPatternType = Union[str, re.Pattern, BotCommand]


class CommandException(Exception):
    pass


class Command(BaseFilter[MessageCreated]):
    __slots__ = (
        "commands",
        "ignore_case",
        "ignore_mention",
        "magic",
        "prefix",
    )

    def __init__(
        self,
        *values: CommandPatternType,
        commands: Sequence[CommandPatternType] | CommandPatternType | None = None,
        prefix: str = "/",
        ignore_case: bool = False,
        ignore_mention: bool = False,
    ) -> None:
        if commands is None:
            commands = []
        if isinstance(commands, (str, re.Pattern, BotCommand)):
            commands = [commands]

        if not isinstance(commands, Iterable):
            raise ValueError(
                "Command filter only supports str, re.Pattern, BotCommand object"
                " or their Iterable"
            )

        items = []
        for command in (*values, *commands):
            if isinstance(command, BotCommand):
                command = command.name
            if not isinstance(command, (str, re.Pattern)):
                raise ValueError(
                    "Command filter only supports str, re.Pattern, BotCommand object"
                    " or their Iterable"
                )
            if ignore_case and isinstance(command, str):
                command = command.casefold()
            items.append(command)

        if not items:
            raise ValueError("At least one command should be specified")

        self.commands = tuple(items)
        self.prefix = prefix
        self.ignore_case = ignore_case
        self.ignore_mention = ignore_mention

    def __str__(self) -> str:
        return self._signature_to_string(
            *self.commands,
            prefix=self.prefix,
            ignore_case=self.ignore_case,
            ignore_mention=self.ignore_mention,
        )

    async def __call__(
        self, message: MessageCreated, bot: Bot
    ) -> Union[bool, Dict[str, Any]]:
        if not isinstance(message, MessageCreated):
            return False

        text = (message.message.body and message.message.body.text) or (
            message.message.link and message.message.link.message.text
        )
        if not text:
            return False

        try:
            command = await self.parse_command(text=text, bot=bot)
        except CommandException:
            return False
        result = {"command": command}
        if command.magic_result and isinstance(command.magic_result, dict):
            result.update(command.magic_result)
        return result

    def extract_command(self, text: str) -> CommandObject:
        try:
            full_command, *args = text.split(maxsplit=1)
        except ValueError:
            raise CommandException("not enough values to unpack")

        prefix, (command, _, mention) = full_command[0], full_command[1:].partition("@")
        return CommandObject(
            prefix=prefix,
            command=command,
            mention=mention or None,
            args=args[0] if args else None,
        )

    def validate_prefix(self, command: CommandObject) -> None:
        if command.prefix not in self.prefix:
            raise CommandException("Invalid command prefix")

    async def validate_mention(self, bot: Bot, command: CommandObject) -> None:
        if command.mention and not self.ignore_mention:
            me = bot.state.info
            if me.username and command.mention.lower() != me.username.lower():
                raise CommandException("Mention did not match")

    def validate_command(self, command: CommandObject) -> CommandObject:
        for allowed_command in cast(Sequence[CommandPatternType], self.commands):
            if isinstance(allowed_command, Pattern):
                result = allowed_command.match(command.command)
                if result:
                    return replace(command, regexp_match=result)

            command_name = command.command
            if self.ignore_case:
                command_name = command_name.casefold()

            if command_name == allowed_command:
                return command
        raise CommandException("Command did not match pattern")

    async def parse_command(self, text: str, bot: Bot) -> CommandObject:
        command = self.extract_command(text)
        self.validate_prefix(command=command)
        await self.validate_mention(bot=bot, command=command)
        command = self.validate_command(command)
        return command


@dataclass(frozen=True)
class CommandObject:
    prefix: str = "/"
    command: str = ""
    mention: str | None = None
    args: str | None = field(repr=False, default=None)
    regexp_match: Match[str] | None = field(repr=False, default=None)

    @property
    def mentioned(self) -> bool:
        return bool(self.mention)

    @property
    def text(self) -> str:
        line = self.prefix + self.command
        if self.mention:
            line += "@" + self.mention
        if self.args:
            line += " " + self.args
        return line


class CommandStart(Command):
    def __init__(
        self,
        deep_link: bool = False,
        deep_link_encoded: bool = False,
        ignore_case: bool = False,
        ignore_mention: bool = False,
    ) -> None:
        super().__init__(
            "start",
            prefix="/",
            ignore_case=ignore_case,
            ignore_mention=ignore_mention,
        )
        self.deep_link = deep_link
        self.deep_link_encoded = deep_link_encoded

    def __str__(self) -> str:
        return self._signature_to_string(
            ignore_case=self.ignore_case,
            ignore_mention=self.ignore_mention,
            deep_link=self.deep_link,
            deep_link_encoded=self.deep_link_encoded,
        )

    async def parse_command(self, text: str, bot: Bot) -> CommandObject:
        command = self.extract_command(text)
        self.validate_prefix(command=command)
        await self.validate_mention(bot=bot, command=command)
        command = self.validate_command(command)
        command = self.validate_deeplink(command=command)
        return command

    def validate_deeplink(self, command: CommandObject) -> CommandObject:
        if not self.deep_link:
            return command
        if not command.args:
            raise CommandException("Deep-link was missing")
        args = command.args
        if self.deep_link_encoded:
            try:
                args = decode_payload(args)
            except UnicodeDecodeError as e:
                raise CommandException(f"Failed to decode Base64: {e}")
            return replace(command, args=args)
        return command
