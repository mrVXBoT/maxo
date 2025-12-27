from maxo.enums import ButtonType
from maxo.types.button import Button


class RequestContactButton(Button):
    """
    Инлайн кнопка запроса контакта.

    Args:
        text: Видимый текст кнопки. От 1 до 128 символов.

    """

    type: ButtonType = ButtonType.REQUEST_CONTACT
