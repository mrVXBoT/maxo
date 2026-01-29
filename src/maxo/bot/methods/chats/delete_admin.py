from maxo.bot.methods.base import MaxoMethod
from maxo.bot.methods.markers import Path
from maxo.types.base import MaxoType
from maxo.types.simple_query_result import SimpleQueryResult


class DeleteAdmin(MaxoMethod[SimpleQueryResult], MaxoType):
    """Отменить права администратора в групповом чате."""

    __url__ = "chats/{chat_id}/members/admins/{user_id}"
    __method__ = "delete"

    chat_id: Path[int]
    user_id: Path[int]
