import operator

import pytest

from maxo.dialogs.widgets.kbd import Toggle
from maxo.dialogs.widgets.text import Format
from maxo.types import MaxoType


@pytest.mark.asyncio
async def test_render_toggle(mock_manager) -> None:
    toggle = Toggle(
        Format("{item[1]}"),
        id="fruit",
        item_id_getter=operator.itemgetter(0),
        items=[("1", "Apple"), ("2", "Banana"), ("3", "Orange")],
    )

    keyboard = await toggle.render_keyboard(
        data={},
        manager=mock_manager,
    )

    assert keyboard[0][0].text == "Apple"

    await toggle.set_checked(MaxoType(), "2", mock_manager)

    keyboard = await toggle.render_keyboard(
        data={},
        manager=mock_manager,
    )

    assert keyboard[0][0].text == "Banana"
