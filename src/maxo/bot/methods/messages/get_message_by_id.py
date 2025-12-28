from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.message import Message


class GetMessageById(MaxoMethod[Message]):
    """Получить сообщение."""

    __url__ = "messages/{message_id}"
    __http_method__ = "get"

    message_id: UrlVar[str]
