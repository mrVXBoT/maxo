from maxo.bot.methods.base import MaxoMethod
from maxo.bot.methods.markers import Path
from maxo.types.base import MaxoType
from maxo.types.chat_members_list import ChatMembersList


class GetAdmins(MaxoMethod[ChatMembersList], MaxoType):
    """Получение списка администраторов группового чата."""

    __url__ = "chats/{chat_id}/members/admins"
    __method__ = "get"

    chat_id: Path[int]
