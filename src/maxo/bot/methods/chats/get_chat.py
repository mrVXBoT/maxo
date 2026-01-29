from maxo.bot.methods.base import MaxoMethod
from maxo.bot.methods.markers import Path
from maxo.types.base import MaxoType
from maxo.types.chat import Chat


class GetChat(MaxoMethod[Chat], MaxoType):
    """Получение информации о групповом чате."""

    __url__ = "chats/{chat_id}"
    __method__ = "get"

    chat_id: Path[int]
