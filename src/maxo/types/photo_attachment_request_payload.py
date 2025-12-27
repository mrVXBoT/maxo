from typing import Any

from maxo.omit import Omittable, Omitted
from maxo.types.base import MaxoType


class PhotoAttachmentRequestPayload(MaxoType):
    """
    Запрос на прикрепление изображения (все поля являются взаимоисключающими).

    Запрос на прикрепление изображения.

    Все поля являются взаимоисключающими.

    Args:
        url: Любой внешний URL изображения, которое вы хотите прикрепить. От 1 символа.
        token: Токен существующего вложения.
        photos: Токены, полученные после загрузки изображений

    """

    url: Omittable[str | None] = Omitted()
    token: Omittable[str | None] = Omitted()
    photos: Omittable[dict[str, Any] | None] = Omitted()
