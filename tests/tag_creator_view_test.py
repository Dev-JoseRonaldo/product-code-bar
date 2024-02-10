import os
from src.views.tag_creator_view import TagCreatorView

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_validate_and_create():
    view = TagCreatorView()
    req = MockRequest(body = {"product_code": "123456"})
    view.validate_and_create(req)
    os.remove('123456.png')

def test_validate_and_create_with_error():
    view = TagCreatorView()
    req = MockRequest(body = {"product_code": 123456})
    try:
        view.validate_and_create(req)
    except Exception as exception:
        assert isinstance(exception, TypeError)
