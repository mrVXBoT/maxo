from retejo.http.markers import QueryParam

from maxo.bot.methods.base import MaxoMethod
from maxo.enums import UploadType
from maxo.types import UploadEndpoint


class GetUploadUrl(MaxoMethod[UploadEndpoint]):
    """
    Получение URL для загрузки файла.

    Возвращает URL для последующей загрузки файла.

    Для видео и аудио токен возвращается в ответе этого метода.
    Для фотографий и файла токен возвращается в ответе
    на загрузку изображения или файла.

    Args:
        type: Тип загружаемого файла.

    """

    __url__ = "uploads"
    __http_method__ = "post"

    type: QueryParam[UploadType]
