from maxo.enums.reply_button_type import ReplyButtonType
from maxo.omit import Omittable, Omitted
from maxo.types.reply_button import ReplyButton


class SendGeoLocationButton(ReplyButton):
    """
    После нажатия на такую кнопку клиент отправляет новое сообщение с вложением текущего географического положения пользователя

    Args:
        quick: Если *true*, отправляет местоположение без запроса подтверждения пользователя
        type:

    """

    type: ReplyButtonType = ReplyButtonType.USER_GEO_LOCATION

    quick: Omittable[bool] = Omitted()
