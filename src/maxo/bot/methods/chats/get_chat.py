from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.chat import Chat


class GetChat(MaxoMethod[Chat]):
    """Получение информации о групповом чате."""

    __url__ = "chats/{chat_id}"
    __http_method__ = "get"

    chat_id: UrlVar[int]
