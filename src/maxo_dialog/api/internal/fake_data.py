from typing import Any, Literal

from maxo.bot.methods import CallbackAnswer
from maxo.tools.facades import MessageCreatedFacade
from maxo.types import (
    Callback,
    Chat,
    User,
)


class ReplyCallback(Callback):
    original_message: MessageCreatedFacade

    def answer(self, *args: Any, **kwargs: Any) -> CallbackAnswer:
        raise ValueError(
            "This callback query is generated from ReplyButton click. "
            "Support of `.answer()` call is impossible.",
        )


class FakeUser(User):
    fake: Literal[True] = True


class FakeChat(Chat):
    fake: Literal[True] = True
