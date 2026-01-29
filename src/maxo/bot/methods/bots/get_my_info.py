from maxo.bot.methods.base import MaxoMethod
from maxo.types.base import MaxoType
from maxo.types.bot_info import BotInfo


class GetMyInfo(MaxoMethod[BotInfo], MaxoType):
    """Получение информации о боте."""

    __url__ = "me"
    __method__ = "get"
