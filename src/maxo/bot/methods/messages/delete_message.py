from maxo.bot.methods.base import MaxoMethod
from maxo.bot.methods.markers import Query
from maxo.types.base import MaxoType
from maxo.types.simple_query_result import SimpleQueryResult


class DeleteMessage(MaxoMethod[SimpleQueryResult], MaxoType):
    """Удалить сообщение."""

    __url__ = "messages"
    __method__ = "delete"

    message_id: Query[str]
