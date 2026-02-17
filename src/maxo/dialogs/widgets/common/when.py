from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Protocol

from maxo.dialogs.api.protocols import DialogManager
from maxo.dialogs.tools.dialog_filter import DialogFilter, is_dialog_filter

if TYPE_CHECKING:
    from maxo.dialogs.integrations.magic_filter import MagicDialogFilter


# Try to import magic_filter
try:
    from magic_filter import MagicFilter as _MagicFilter
    _HAS_MAGIC_FILTER = True
except ImportError:  # pragma: no cover
    _HAS_MAGIC_FILTER = False
    _MagicFilter = None  # type: ignore[misc, assignment]


class Predicate(Protocol):
    @abstractmethod
    def __call__(
        self,
        data: dict,
        widget: Whenable,
        dialog_manager: DialogManager,
        /,
    ) -> bool:
        """
        Check if widget should be shown.

        :param data: Data received from getter
        :param widget: Widget we are working with
        :param dialog_manager: Dialog manager to access current context
        :return: ``True`` if widget has to be shown, ``False`` otherwise
        """
        raise NotImplementedError


# Type alias that supports DialogFilter or magic_filter.MagicFilter
WhenCondition = str | DialogFilter | Predicate | None


def new_when_field(fieldname: str) -> Predicate:
    def when_field(
        data: dict,
        widget: Whenable,
        manager: DialogManager,
    ) -> bool:
        return bool(data.get(fieldname))

    return when_field


def new_when_dialog_filter(f: DialogFilter) -> Predicate:
    def when_filter(
        data: dict,
        widget: Whenable,
        manager: DialogManager,
    ) -> bool:
        return bool(f.resolve(data))

    return when_filter


def true_condition(data: dict, widget: Whenable, manager: DialogManager) -> bool:
    return True


class Whenable:
    def __init__(self, when: WhenCondition = None) -> None:
        self.condition: Predicate
        if when is None:
            self.condition = true_condition
        elif isinstance(when, str):
            self.condition = new_when_field(when)
        elif is_dialog_filter(when):
            self.condition = new_when_dialog_filter(when)
        elif _HAS_MAGIC_FILTER and isinstance(when, _MagicFilter):
            # Handle magic_filter.MagicFilter if available
            from maxo.dialogs.integrations.magic_filter import MagicDialogFilter
            self.condition = new_when_dialog_filter(MagicDialogFilter(when))
        else:
            self.condition = when

    def is_(self, data: dict, manager: DialogManager) -> bool:
        return self.condition(data, self, manager)
