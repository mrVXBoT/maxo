import asyncio
import inspect
from collections.abc import Callable
from dataclasses import dataclass, field
from functools import partial
from typing import TYPE_CHECKING, Any

from maxo.dialogs.tools.dialog_filter import DialogFilter, is_dialog_filter
from maxo.routing.interfaces import Filter

if TYPE_CHECKING:
    from maxo.dialogs.integrations.magic_filter import MagicDialogFilter

CallbackType = Callable[..., Any]

# Try to import magic_filter
try:
    from magic_filter.magic import MagicFilter as OriginalMagicFilter
    _HAS_MAGIC_FILTER = True
except ImportError:  # pragma: no cover
    _HAS_MAGIC_FILTER = False
    OriginalMagicFilter = None  # type: ignore[misc, assignment]


@dataclass
class CallableObject:
    callback: CallbackType
    awaitable: bool = field(init=False)
    params: set[str] = field(init=False)
    varkw: bool = field(init=False)

    def __post_init__(self) -> None:
        callback = inspect.unwrap(self.callback)
        self.awaitable = inspect.isawaitable(callback) or inspect.iscoroutinefunction(
            callback,
        )
        spec = inspect.getfullargspec(callback)
        self.params = {*spec.args, *spec.kwonlyargs}
        self.varkw = spec.varkw is not None

    def _prepare_kwargs(self, kwargs: dict[str, Any]) -> dict[str, Any]:
        if self.varkw:
            return kwargs

        return {k: kwargs[k] for k in self.params if k in kwargs}

    async def call(self, *args: Any, **kwargs: Any) -> Any:
        wrapped = partial(self.callback, *args, **self._prepare_kwargs(kwargs))
        if self.awaitable:
            return await wrapped()
        return await asyncio.to_thread(wrapped)


@dataclass
class FilterObject(CallableObject):
    magic: "MagicDialogFilter | DialogFilter | None" = None

    def __post_init__(self) -> None:
        # Check if callback is a magic_filter.MagicFilter
        if _HAS_MAGIC_FILTER and isinstance(self.callback, OriginalMagicFilter):
            # Import here to avoid circular imports and make it optional
            from maxo.dialogs.integrations.magic_filter import MagicDialogFilter
            self.magic = MagicDialogFilter(self.callback)
            self.callback = self.magic.resolve
        elif is_dialog_filter(self.callback):
            self.magic = self.callback
            self.callback = self.callback.resolve

        super().__post_init__()

        if isinstance(self.callback, Filter):
            self.awaitable = True
