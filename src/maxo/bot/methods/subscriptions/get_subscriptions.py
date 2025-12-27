from maxo.bot.methods.base import MaxoMethod
from maxo.types.get_subscriptions_result import GetSubscriptionsResult


class GetSubscriptions(MaxoMethod[GetSubscriptionsResult]):
    """Получение подписок."""

    __url__ = "subscriptions"
    __http_method__ = "get"
