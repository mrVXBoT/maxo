from datetime import datetime

from maxo.enums import UpdateType
from maxo.types.base import MaxoType


class BaseUpdate(MaxoType):
    pass


class MaxUpdate(BaseUpdate):
    type: UpdateType
    timestamp: datetime
