from retejo.http.markers import Body, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.simple_query_result import SimpleQueryResult


class PinMessage(MaxoMethod[SimpleQueryResult]):
    """Закрепление сообщения в групповом чате."""

    __url__ = "chats/{chat_id}/pin"
    __http_method__ = "put"

    chat_id: UrlVar[int]

    message_id: Body[str]
    notify: Body[Omittable[bool | None]] = Omitted()
