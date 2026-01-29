from maxo.bot.methods.base import MaxoMethod
from maxo.types.base import MaxoType
from maxo.types.get_subscriptions_result import GetSubscriptionsResult


class GetSubscriptions(MaxoMethod[GetSubscriptionsResult], MaxoType):
    """Получение подписок."""

    __url__ = "subscriptions"
    __method__ = "get"
