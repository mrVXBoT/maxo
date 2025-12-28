from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class UnpinMessage(MaxoMethod[SimpleQueryResult]):
    """Удаление закреплённого сообщения в групповом чате."""

    __url__ = "chats/{chat_id}/pin"
    __http_method__ = "delete"

    chat_id: UrlVar[int]
