from maxo.enums.button_type import ButtonType
from maxo.omit import Omittable, Omitted
from maxo.types.button import Button


class OpenAppButton(Button):
    """
    Кнопка для запуска мини-приложения.
    Инлайн кнопка для открытия приложения.
    """

    type: ButtonType = ButtonType.OPEN_APP

    web_app: Omittable[str] = Omitted()
    contact_id: Omittable[int] = Omitted()
    payload: Omittable[str] = Omitted()
