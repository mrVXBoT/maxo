from maxo.omit import Omittable, Omitted
from maxo.types.base import MaxoType


class UploadEndpoint(MaxoType):
    """
    Это информация, которую вы получите, как только аудио/видео будет загружено.
    Загруженная информация.

    Args:
        token: Токен — уникальный ID загруженного медиафайла.

    """

    token: Omittable[str] = Omitted()
