from maxo.enums.chat_type import ChatType
from maxo.types.base import MaxoType


class Recipient(MaxoType):
    """
    Новый получатель сообщения. Может быть пользователем или чатом.
    Получатель сообщения.

    Args:
        chat_type: Тип чата.
        user_id: ID пользователя, если сообщение было отправлено пользователю.
        chat_id: ID чата.

    """

    chat_id: int | None = None
    chat_type: ChatType
    user_id: int | None = None
