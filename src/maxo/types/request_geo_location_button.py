from maxo.enums.button_type import ButtonType
from maxo.omit import Omittable, Omitted
from maxo.types.button import Button


class RequestGeoLocationButton(Button):
    """
    После нажатия на такую кнопку клиент отправляет новое сообщение с вложением текущего географического положения пользователя.
    Инлайн кнопка запроса геолокации.

    Args:
       text: Видимый текст кнопки. От 1 до 128 символов.
       quick: Если true, отправляет местоположение без запроса подтверждения пользователя.

    """

    type: ButtonType = ButtonType.REQUEST_GEO_LOCATION
    quick: Omittable[bool] = Omitted()
