from maxo.bot.methods.base import MaxoMethod
from maxo.bot.methods.markers import Query
from maxo.enums.upload_type import UploadType
from maxo.types.base import MaxoType
from maxo.types.upload_endpoint import UploadEndpoint


class GetUploadUrl(MaxoMethod[UploadEndpoint], MaxoType):
    """Загрузка файлов."""

    __url__ = "uploads"
    __method__ = "post"

    type: Query[UploadType]
