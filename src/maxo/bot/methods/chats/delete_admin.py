from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class DeleteAdmin(MaxoMethod[SimpleQueryResult]):
    """Отменить права администратора в групповом чате."""

    __url__ = "chats/{chat_id}/members/admins/{user_id}"
    __http_method__ = "delete"

    chat_id: UrlVar[int]
    user_id: UrlVar[int]
