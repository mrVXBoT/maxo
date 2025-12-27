from maxo.enums.button_type import ButtonType
from maxo.omit import Omittable, Omitted
from maxo.types.button import Button


class MessageButton(Button):
    """
    Инлайн кнопка, текст которого будет отправлен в чат.

    Args:
        text: Текст кнопки, который будет отправлен в чат от лица пользователя. От 1 до 128 символов.

    """

    type: ButtonType = ButtonType.MESSAGE

    text: Omittable[str] = Omitted()
