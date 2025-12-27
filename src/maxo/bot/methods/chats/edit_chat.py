from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.chat import Chat


class EditChat(MaxoMethod[Chat]):
    """Изменение информации о групповом чате."""

    __url__ = "chats/{chat_id}"
    __http_method__ = "patch"

    chat_id: UrlVar[int]
