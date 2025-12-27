from retejo.http.markers import QueryParam, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.chat_members_list import ChatMembersList


class GetMembers(MaxoMethod[ChatMembersList]):
    """
    Получение участников группового чата.
    Получение участников чата.

    Возвращает пользователей, участвующих в чате.

    Источник: https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members

    Args:
        chat_id: ID чата.
        user_ids:
            Список ID пользователей, чье членство нужно получить.
            Когда этот параметр передан, параметры `count` и `marker` игнорируются.
        marker: Указатель на следующую страницу данных.
        count: Количество участников, которых нужно вернуть. По умолчанию: `20`.

    """

    __url__ = "chats/{chat_id}/members"
    __http_method__ = "get"

    chat_id: UrlVar[int]
    user_ids: QueryParam[Omittable[list[int] | None]] = Omitted()
    marker: QueryParam[Omittable[int]] = Omitted()
    count: QueryParam[Omittable[int]] = Omitted()
