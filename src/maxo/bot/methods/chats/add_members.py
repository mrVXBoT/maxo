from retejo.http.markers import Body, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class AddMembers(MaxoMethod[SimpleQueryResult]):
    """Добавление участников в групповой чат."""

    __url__ = "chats/{chat_id}/members"
    __http_method__ = "post"

    chat_id: UrlVar[int]

    user_ids: Body[list[int]]
