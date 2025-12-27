from retejo.http.entities import FileObj
from retejo.http.markers import Form, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.upload_endpoint import UploadEndpoint


class UploadMedia(MaxoMethod[UploadEndpoint]):
    """
    Загрузка медиа.

    Args:
        upload_url: URL для загрузки медиа.
        file: Загружаемый файл.

    """

    __url__ = "{upload_url}"
    __http_method__ = "post"

    upload_url: UrlVar[str]
    file: Form[FileObj]
