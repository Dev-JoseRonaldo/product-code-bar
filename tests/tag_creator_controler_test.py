from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from src.controllers.tag_creator_controler import TagCreatorController

@patch.object(BarcodeHandler, "create_barcode")
def test_create(mock_create_barcode):
    mock_value = "image_path"
    mock_create_barcode.return_value = mock_value
    tag_creator_controler = TagCreatorController()

    result = tag_creator_controler.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f"{mock_value}.png"
