from retejo.http.markers import Body, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.chat import Chat
from maxo.types.photo_attachment_request_payload import PhotoAttachmentRequestPayload


class EditChat(MaxoMethod[Chat]):
    """Изменение информации о групповом чате."""

    __url__ = "chats/{chat_id}"
    __http_method__ = "patch"

    chat_id: UrlVar[int]

    icon: Body[Omittable[PhotoAttachmentRequestPayload | None]] = Omitted()
    notify: Body[Omittable[bool | None]] = Omitted()
    pin: Body[Omittable[str | None]] = Omitted()
    title: Body[Omittable[str | None]] = Omitted()
