from collections.abc import Callable, Hashable
from typing import TYPE_CHECKING, Any

from maxo.dialogs.api.protocols import DialogManager
from maxo.dialogs.tools.dialog_filter import DialogFilter, is_dialog_filter
from maxo.dialogs.widgets.common import WhenCondition

if TYPE_CHECKING:
    from maxo.dialogs.integrations.magic_filter import MagicDialogFilter


# Try to import magic_filter
try:
    from magic_filter import MagicFilter as _MagicFilter
    _HAS_MAGIC_FILTER = True
except ImportError:  # pragma: no cover
    _HAS_MAGIC_FILTER = False
    _MagicFilter = None  # type: ignore[misc, assignment]

from .base import Text

Selector = Callable[[dict, "Case", DialogManager], Hashable]


def new_case_field(fieldname: str) -> Selector:
    def case_field(
        data: dict,
        widget: "Case",
        manager: DialogManager,
    ) -> Hashable:
        return data.get(fieldname)

    return case_field


def new_dialog_filter_selector(f: DialogFilter) -> Selector:
    def filter_selector(
        data: dict,
        widget: "Case",
        manager: DialogManager,
    ) -> Hashable:
        return f.resolve(data)

    return filter_selector


class Case(Text):
    def __init__(
        self,
        texts: dict[Any, Text],
        selector: str | Selector | DialogFilter,
        when: WhenCondition = None,
    ) -> None:
        super().__init__(when=when)
        self.texts = texts
        if isinstance(selector, str):
            self.selector = new_case_field(selector)
        elif is_dialog_filter(selector):
            self.selector = new_dialog_filter_selector(selector)
        elif _HAS_MAGIC_FILTER and isinstance(selector, _MagicFilter):
            # Handle magic_filter.MagicFilter if available
            from maxo.dialogs.integrations.magic_filter import MagicDialogFilter
            self.selector = new_dialog_filter_selector(MagicDialogFilter(selector))
        else:
            self.selector = selector
        self._has_default = ... in self.texts

    async def _render_text(self, data: dict, manager: DialogManager) -> str:
        selection = self.selector(data, self, manager)
        if selection not in self.texts:
            if self._has_default:
                selection = ...
            elif manager.is_preview():
                selection = next(iter(self.texts))
        return await self.texts[selection].render_text(data, manager)

    def find(self, widget_id: str) -> Text | None:
        for text in self.texts.values():
            if found := text.find(widget_id):
                return found
        return None
