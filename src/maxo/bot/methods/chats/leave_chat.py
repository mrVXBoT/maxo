from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class LeaveChat(MaxoMethod[SimpleQueryResult]):
    """Удаление бота из группового чата."""

    __url__ = "chats/{chat_id}/members/me"
    __http_method__ = "delete"

    chat_id: UrlVar[int]
