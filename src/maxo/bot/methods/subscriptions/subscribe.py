from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class Subscribe(MaxoMethod[SimpleQueryResult]):
    """Подписка на обновления."""

    __url__ = "subscriptions"
    __http_method__ = "post"
