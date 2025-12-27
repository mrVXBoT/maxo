from maxo.types.base import MaxoType
from maxo.types.buttons import InlineButtons


class InlineKeyboardAttachmentRequestPayload(MaxoType):
    """
    Полезная нагрузка для запроса на прикрепление inline клавиатуры.

    Args:
        buttons: Двумерный массив кнопок. От 1 элемента

    """

    buttons: list[list[InlineButtons]]
