import json
from collections.abc import Callable, Sequence
from datetime import datetime
from typing import Any

from adaptix import P, Retort, dumper, loader
from aiohttp import ClientSession
from unihttp.clients.aiohttp import AiohttpAsyncClient
from unihttp.http import HTTPResponse
from unihttp.markers import BodyMarker, QueryMarker
from unihttp.method import BaseMethod
from unihttp.middlewares import AsyncMiddleware
from unihttp.serializers.adaptix import DEFAULT_RETORT

from maxo._internal._adaptix.concat_provider import concat_provider
from maxo._internal._adaptix.has_tag_provider import has_tag_provider
from maxo.bot.warming_up import WarmingUpType, warming_up_retort
from maxo.enums import (
    AttachmentRequestType,
    AttachmentType,
    ButtonType,
    MarkupElementType,
    UpdateType,
)
from maxo.enums.text_format import TextFormat
from maxo.errors import MaxBotApiError
from maxo.errors.api import (
    MaxBotBadRequestError,
    MaxBotForbiddenError,
    MaxBotMethodNotAllowedError,
    MaxBotNotFoundError,
    MaxBotServiceUnavailableError,
    MaxBotTooManyRequestsError,
    MaxBotUnauthorizedError,
    MaxBotUnknownServerError,
)
from maxo.omit import Omittable
from maxo.routing.updates import (
    BotStopped,
    DialogCleared,
    DialogMuted,
    DialogRemoved,
    DialogUnmuted,
)
from maxo.routing.updates.bot_added_to_chat import BotAddedToChat
from maxo.routing.updates.bot_removed_from_chat import BotRemovedFromChat
from maxo.routing.updates.bot_started import BotStarted
from maxo.routing.updates.chat_title_changed import ChatTitleChanged
from maxo.routing.updates.message_callback import MessageCallback
from maxo.routing.updates.message_chat_created import MessageChatCreated
from maxo.routing.updates.message_created import MessageCreated
from maxo.routing.updates.message_edited import MessageEdited
from maxo.routing.updates.message_removed import MessageRemoved
from maxo.routing.updates.user_added_to_chat import UserAddedToChat
from maxo.routing.updates.user_removed_from_chat import UserRemovedFromChat
from maxo.types import (
    DataAttachment,
    InlineKeyboardAttachment,
    ReplyKeyboardAttachment,
    ReplyKeyboardAttachmentRequest,
)
from maxo.types.audio_attachment import AudioAttachment
from maxo.types.audio_attachment_request import AudioAttachmentRequest
from maxo.types.callback_button import CallbackButton
from maxo.types.contact_attachment import ContactAttachment
from maxo.types.contact_attachment_request import ContactAttachmentRequest
from maxo.types.file_attachment import FileAttachment
from maxo.types.file_attachment_request import FileAttachmentRequest
from maxo.types.inline_keyboard_attachment_request import (
    InlineKeyboardAttachmentRequest,
)
from maxo.types.link_button import LinkButton
from maxo.types.location_attachment import LocationAttachment
from maxo.types.location_attachment_request import LocationAttachmentRequest
from maxo.types.markup_elements import (
    EmphasizedMarkupElement,
    LinkMarkupElement,
    MonospacedMarkupElements,
    StrikethroughMarkupElement,
    StrongMarkupElement,
    UnderlineMarkupElement,
    UserMentionMarkupElement,
)
from maxo.types.message_button import MessageButton
from maxo.types.open_app_button import OpenAppButton
from maxo.types.photo_attachment import PhotoAttachment
from maxo.types.photo_attachment_request import PhotoAttachmentRequest
from maxo.types.request_contact_button import RequestContactButton
from maxo.types.request_geo_location_button import RequestGeoLocationButton
from maxo.types.share_attachment import ShareAttachment
from maxo.types.share_attachment_request import ShareAttachmentRequest
from maxo.types.sticker_attachment import StickerAttachment
from maxo.types.sticker_attachment_request import StickerAttachmentRequest
from maxo.types.video_attachment import VideoAttachment
from maxo.types.video_attachment_request import VideoAttachmentRequest

_has_tag_providers = concat_provider(
    # ---> UpdateType <---
    has_tag_provider(BotAddedToChat, "update_type", UpdateType.BOT_ADDED),
    has_tag_provider(BotRemovedFromChat, "update_type", UpdateType.BOT_REMOVED),
    has_tag_provider(BotStarted, "update_type", UpdateType.BOT_STARTED),
    has_tag_provider(BotStopped, "update_type", UpdateType.BOT_STOPPED),
    has_tag_provider(ChatTitleChanged, "update_type", UpdateType.CHAT_TITLE_CHANGED),
    has_tag_provider(DialogCleared, "update_type", UpdateType.DIALOG_CLEARED),
    has_tag_provider(DialogMuted, "update_type", UpdateType.DIALOG_MUTED),
    has_tag_provider(DialogRemoved, "update_type", UpdateType.DIALOG_REMOVED),
    has_tag_provider(DialogUnmuted, "update_type", UpdateType.DIALOG_UNMUTED),
    has_tag_provider(MessageCallback, "update_type", UpdateType.MESSAGE_CALLBACK),
    has_tag_provider(
        MessageChatCreated,
        "update_type",
        UpdateType.MESSAGE_CHAT_CREATED,
    ),
    has_tag_provider(MessageCreated, "update_type", UpdateType.MESSAGE_CREATED),
    has_tag_provider(MessageEdited, "update_type", UpdateType.MESSAGE_EDITED),
    has_tag_provider(MessageRemoved, "update_type", UpdateType.MESSAGE_REMOVED),
    has_tag_provider(UserAddedToChat, "update_type", UpdateType.USER_ADDED),
    has_tag_provider(UserRemovedFromChat, "update_type", UpdateType.USER_REMOVED),
    # ---> AttachmentType <---
    has_tag_provider(AudioAttachment, "type", AttachmentType.AUDIO),
    has_tag_provider(ContactAttachment, "type", AttachmentType.CONTACT),
    has_tag_provider(FileAttachment, "type", AttachmentType.FILE),
    has_tag_provider(PhotoAttachment, "type", AttachmentType.IMAGE),
    has_tag_provider(InlineKeyboardAttachment, "type", AttachmentType.INLINE_KEYBOARD),
    has_tag_provider(ReplyKeyboardAttachment, "type", AttachmentType.REPLY_KEYBOARD),
    has_tag_provider(LocationAttachment, "type", AttachmentType.LOCATION),
    has_tag_provider(ShareAttachment, "type", AttachmentType.SHARE),
    has_tag_provider(StickerAttachment, "type", AttachmentType.STICKER),
    has_tag_provider(VideoAttachment, "type", AttachmentType.VIDEO),
    has_tag_provider(DataAttachment, "type", AttachmentType.DATA),
    # ---> MarkupElementType <---
    has_tag_provider(EmphasizedMarkupElement, "type", MarkupElementType.EMPHASIZED),
    # has_tag_provider(HeadingMarkupElement, "type", MarkupElementType.HEADING),
    # has_tag_provider(HighlightedMarkupElement, "type", MarkupElementType.HIGHLIGHTED),
    has_tag_provider(LinkMarkupElement, "type", MarkupElementType.LINK),
    has_tag_provider(MonospacedMarkupElements, "type", MarkupElementType.MONOSPACED),
    has_tag_provider(
        StrikethroughMarkupElement,
        "type",
        MarkupElementType.STRIKETHROUGH,
    ),
    has_tag_provider(StrongMarkupElement, "type", MarkupElementType.STRONG),
    has_tag_provider(UnderlineMarkupElement, "type", MarkupElementType.UNDERLINE),
    has_tag_provider(UserMentionMarkupElement, "type", MarkupElementType.USER_MENTION),
    # ---> AttachmentRequestType <---
    has_tag_provider(PhotoAttachmentRequest, "type", AttachmentRequestType.IMAGE),
    has_tag_provider(VideoAttachmentRequest, "type", AttachmentRequestType.VIDEO),
    has_tag_provider(AudioAttachmentRequest, "type", AttachmentRequestType.AUDIO),
    has_tag_provider(FileAttachmentRequest, "type", AttachmentRequestType.FILE),
    has_tag_provider(StickerAttachmentRequest, "type", AttachmentRequestType.STICKER),
    has_tag_provider(ContactAttachmentRequest, "type", AttachmentRequestType.CONTACT),
    has_tag_provider(
        InlineKeyboardAttachmentRequest,
        "type",
        AttachmentRequestType.INLINE_KEYBOARD,
    ),
    has_tag_provider(
        ReplyKeyboardAttachmentRequest,
        "type",
        AttachmentRequestType.REPLY_KEYBOARD,
    ),
    has_tag_provider(LocationAttachmentRequest, "type", AttachmentRequestType.LOCATION),
    has_tag_provider(ShareAttachmentRequest, "type", AttachmentRequestType.SHARE),
    # ---> KeyboardButtonType <---
    has_tag_provider(CallbackButton, "type", ButtonType.CALLBACK),
    has_tag_provider(LinkButton, "type", ButtonType.LINK),
    has_tag_provider(
        RequestContactButton,
        "type",
        ButtonType.REQUEST_CONTACT,
    ),
    has_tag_provider(
        RequestGeoLocationButton,
        "type",
        ButtonType.REQUEST_GEO_LOCATION,
    ),
    has_tag_provider(
        OpenAppButton,
        "type",
        ButtonType.OPEN_APP,
    ),
    has_tag_provider(
        MessageButton,
        "type",
        ButtonType.MESSAGE,
    ),
)


class MaxApiClient(AiohttpAsyncClient):
    def __init__(
        self,
        token: str,
        warming_up: bool,
        text_format: TextFormat | None = None,
        base_url: str = "https://platform-api.max.ru/",
        middleware: list[AsyncMiddleware] | None = None,
        session: ClientSession | None = None,
        json_dumps: Callable[[Any], str] = json.dumps,
        json_loads: Callable[[str | bytes | bytearray], Any] = json.loads,
    ) -> None:
        self._token = token
        self._warming_up = warming_up
        self._text_format = text_format

        if session is None:
            session = ClientSession()

        if "access_token" not in session._default_headers:
            session._default_headers.update({"authorization": self._token})

        request_dumper = self._init_method_dumper()
        response_loader = self._init_response_loader()

        super().__init__(
            base_url=base_url,
            request_dumper=request_dumper,
            response_loader=response_loader,
            middleware=middleware,
            session=session,
            json_dumps=json_dumps,
            json_loads=json_loads,
        )

    def _init_method_dumper(self) -> Retort:
        retort = DEFAULT_RETORT.extend(
            recipe=[
                _has_tag_providers,
                dumper(P[QueryMarker], lambda _: "null"),
                dumper(P[QueryMarker][bool], lambda item: int(item)),
                dumper(
                    P[QueryMarker][Sequence[str] | Sequence[int]],
                    lambda item: ",".join(item),
                ),
                dumper(
                    P[BodyMarker][Omittable[TextFormat | None]],
                    lambda item: item or self._text_format,
                ),
            ],
        )

        if self._warming_up:
            retort = warming_up_retort(retort, warming_up=WarmingUpType.METHOD)

        return retort

    def _init_response_loader(self) -> Retort:
        retort = DEFAULT_RETORT.extend(
            recipe=[
                _has_tag_providers,
                loader(P[datetime], lambda x: datetime.fromtimestamp(x / 1000)),
            ],
        )

        if self._warming_up:
            retort = warming_up_retort(retort, warming_up=WarmingUpType.TYPES)

        return retort

    def handle_error(self, response: HTTPResponse, method: BaseMethod[Any]):
        code: str = response.data.get("code", "")
        error: str = response.data.get("error", "")
        message: str = response.data.get("message", "")

        if response.status_code == 400:
            raise MaxBotBadRequestError(code, error, message)
        if response.status_code == 401:
            raise MaxBotUnauthorizedError(code, error, message)
        if response.status_code == 403:
            raise MaxBotForbiddenError(code, error, message)
        if response.status_code == 404:
            raise MaxBotNotFoundError(code, error, message)
        if response.status_code == 405:
            raise MaxBotMethodNotAllowedError(code, error, message)
        if response.status_code == 429:
            raise MaxBotTooManyRequestsError(code, error, message)
        if response.status_code == 500:
            raise MaxBotUnknownServerError(code, error, message)
        if response.status_code == 503:
            raise MaxBotServiceUnavailableError(code, error, message)

        raise MaxBotApiError(code, error, message)
