from retejo.http.markers import QueryParam

from maxo.bot.methods.base import MaxoMethod
from maxo.enums.upload_type import UploadType
from maxo.types.upload_endpoint import UploadEndpoint


class GetUploadUrl(MaxoMethod[UploadEndpoint]):
    """Загрузка файлов."""

    __url__ = "uploads"
    __http_method__ = "post"

    type: QueryParam[UploadType]
