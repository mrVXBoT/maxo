from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

from maxo.enums import AttachmentType
from maxo.types import Chat
from maxo.types.keyboard_buttons import KeyboardButtons
from maxo_dialog.api.entities import MediaAttachment, ShowMode
from maxo_dialog.api.entities.link_preview import LinkPreviewOptions

MarkupVariant = list[list[KeyboardButtons]]


class UnknownText(Enum):
    UNKNOWN = object()


@dataclass
class OldMessage:
    chat: Chat
    message_id: str
    media_id: Optional[str]
    media_uniq_id: Optional[str]
    text: Union[str, None, UnknownText] = None
    has_protected_content: Optional[bool] = None
    has_reply_keyboard: bool = False
    business_connection_id: Optional[str] = None
    content_type: Optional[AttachmentType] = None


@dataclass
class NewMessage:
    chat: Chat
    thread_id: Optional[int] = None
    business_connection_id: Optional[str] = None
    text: Optional[str] = None
    reply_markup: Optional[MarkupVariant] = None
    parse_mode: Optional[str] = None
    protect_content: Optional[bool] = None
    show_mode: ShowMode = ShowMode.AUTO
    media: Optional[MediaAttachment] = None
    link_preview_options: Optional[LinkPreviewOptions] = None
