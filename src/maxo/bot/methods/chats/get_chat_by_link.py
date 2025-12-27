from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.chat import Chat


class GetChatByLink(MaxoMethod[Chat]):
    """Получение группового чата по ссылке."""

    __url__ = "chats/{chat_link}"
    __http_method__ = "get"

    chat_link: UrlVar[str]
