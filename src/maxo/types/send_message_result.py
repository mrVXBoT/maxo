from maxo.types.base import MaxoType
from maxo.types.message import Message


class SendMessageResult(MaxoType):
    """
    Результат отправления сообщения.

    Args:
        message: Сообщение

    """

    message: Message
