from dataclasses import dataclass
from typing import Any, Union

from maxo import Bot
from maxo.routing.signals.exception import ExceptionEvent
from maxo.routing.updates import UserAdded, UserRemoved
from maxo.tools.facades import MessageCallbackFacade, MessageCreatedFacade
from maxo.types import Chat, User

from .update_event import DialogUpdateEvent

ChatEvent = Union[
    MessageCallbackFacade,
    UserAdded,
    UserRemoved,
    DialogUpdateEvent,
    ExceptionEvent[Any],
    MessageCreatedFacade,
]


@dataclass
class EventContext:
    bot: Bot
    chat: Chat
    user: User


EVENT_CONTEXT_KEY = "aiogd_event_context"
