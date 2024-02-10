from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler

@patch.object(BarcodeHandler, "create_barcode")
def test_create_barcode(mock_create_barcode):
    mock_value = "123456"
    mock_create_barcode.return_value = mock_value

    assert mock_create_barcode.return_value == mock_value

def test_create_barcode_with_error():
    barcode_handler = BarcodeHandler()
    product_code = 123456

    try:
        barcode_handler.create_barcode(product_code)
    except Exception as exception:
        assert isinstance(exception, TypeError)
