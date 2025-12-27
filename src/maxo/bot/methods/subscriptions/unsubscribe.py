from retejo.http.markers import QueryParam

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class Unsubscribe(MaxoMethod[SimpleQueryResult]):
    """Отписка от обновлений."""

    __url__ = "subscriptions"
    __http_method__ = "delete"

    url: QueryParam[str]
