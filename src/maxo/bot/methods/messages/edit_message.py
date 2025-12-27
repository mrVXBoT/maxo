from retejo.http.markers import QueryParam

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class EditMessage(MaxoMethod[SimpleQueryResult]):
    """Редактировать сообщение."""

    __url__ = "messages"
    __http_method__ = "put"

    message_id: QueryParam[str]
