from unittest.mock import AsyncMock

import pytest

from maxo.dialogs.widgets.kbd import Checkbox
from maxo.dialogs.widgets.text import Const
from maxo.types import MaxoType


@pytest.mark.asyncio
async def test_check_checkbox(mock_manager) -> None:
    checkbox = Checkbox(
        Const("✓  Checked"),
        Const("Unchecked"),
        id="check",
        default=True,
    )

    assert checkbox.is_checked(mock_manager)

    await checkbox.set_checked(MaxoType(), False, mock_manager)

    assert not checkbox.is_checked(mock_manager)


@pytest.mark.asyncio
async def test_on_state_changed_checkbox(mock_manager) -> None:
    on_state_changed = AsyncMock()
    checkbox = Checkbox(
        Const("✓  Checked"),
        Const("Unchecked"),
        id="check",
        on_state_changed=on_state_changed,
    )

    await checkbox.set_checked(MaxoType(), False, mock_manager)

    on_state_changed.assert_called_once()
