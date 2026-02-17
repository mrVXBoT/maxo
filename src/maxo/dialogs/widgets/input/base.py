from abc import abstractmethod
from collections.abc import Awaitable, Callable, Sequence
from typing import TYPE_CHECKING, Any

from maxo.dialogs.api.internal import InputWidget
from maxo.dialogs.api.protocols import (
    DialogManager,
    DialogProtocol,
)
from maxo.dialogs.tools.filter_object import FilterObject
from maxo.dialogs.widgets.common import Actionable
from maxo.dialogs.widgets.widget_event import (
    WidgetEventProcessor,
    ensure_event_processor,
)
from maxo.enums import AttachmentType
from maxo.routing.updates import MessageCreated
from maxo.types import Message

if TYPE_CHECKING:
    from maxo.integrations.magic_filter import MagicFilter


# Try to import magic_filter
try:
    from magic_filter import F as _F
    _HAS_MAGIC_FILTER = True
except ImportError:  # pragma: no cover
    _HAS_MAGIC_FILTER = False
    _F = None  # type: ignore[misc]


MessageHandlerFunc = Callable[
    [Message, "MessageInput", DialogManager],
    Awaitable,
]


class BaseInput(Actionable, InputWidget):
    @abstractmethod
    async def process_message(
        self,
        message: MessageCreated,
        dialog: DialogProtocol,
        manager: DialogManager,
    ) -> bool:
        raise NotImplementedError


class MessageInput(BaseInput):
    def __init__(
        self,
        func: MessageHandlerFunc | WidgetEventProcessor | None,
        content_types: Sequence[AttachmentType] | AttachmentType | None = None,
        filter: Callable[..., Any] | None = None,
        id: str | None = None,
    ) -> None:
        super().__init__(id=id)
        self.func = ensure_event_processor(func)

        # TODO: Починить. `F.content_type` не существует
        filters = []
        if content_types is not None and _HAS_MAGIC_FILTER:
            # Only use MagicFilter integration if magic_filter is installed
            from maxo.integrations.magic_filter import MagicFilter as _MagicFilter
            if isinstance(content_types, str):
                filters.append(
                    FilterObject(_MagicFilter(_F.content_type == content_types)),
                )
            else:
                filters.append(
                    FilterObject(_MagicFilter(_F.content_type.in_(content_types))),
                )
        if filter is not None:
            filters.append(FilterObject(filter))
        self.filters = filters

    async def process_message(
        self,
        message: MessageCreated,
        dialog: DialogProtocol,
        manager: DialogManager,
    ) -> bool:
        for handler_filter in self.filters:
            if not await handler_filter.call(
                manager.event,
                **manager.middleware_data,
            ):
                return False
        await self.func.process_event(message, self, manager)
        return True
