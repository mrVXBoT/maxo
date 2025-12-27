from maxo.enums import ButtonType
from maxo.types.button import Button


class LinkButton(Button):
    """
    После нажатия на такую кнопку пользователь переходит по ссылке, которую она содержит.
    Инлайн кнопка с ссылкой.

    Args:
        text: Видимый текст кнопки. От 1 до 128 символов.
        url: Ссылка. до 2048 символов

    """

    type: ButtonType = ButtonType.LINK

    text: str
    url: str
