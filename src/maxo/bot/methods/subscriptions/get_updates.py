from retejo.http.markers import QueryParam

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.update_list import UpdateList


class GetUpdates(MaxoMethod[UpdateList]):
    """Получение обновлений."""

    __url__ = "updates"
    __http_method__ = "get"

    limit: QueryParam[Omittable[int]] = Omitted()
    marker: QueryParam[Omittable[int | None]] = Omitted()
    timeout: QueryParam[Omittable[int]] = Omitted()
    types: QueryParam[Omittable[list[str] | None]] = Omitted()
