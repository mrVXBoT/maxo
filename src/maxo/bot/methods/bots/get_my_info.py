from maxo.bot.methods.base import MaxoMethod
from maxo.types.bot_info import BotInfo


class GetMyInfo(MaxoMethod[BotInfo]):
    """
    Получение информации о текущем боте.

    Возвращает информацию о текущем боте,
    который идентифицируется с помощью токена доступа.
    Метод возвращает ID бота, его имя и аватар (если есть).

    Источник: https://dev.max.ru/docs-api/methods/GET/me
    """

    __url__ = "me"
    __http_method__ = "get"
