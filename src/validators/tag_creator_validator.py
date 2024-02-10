from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def tag_creator_validator(request: any) -> None:
    body_validator = Validator({
        "product_code": {
            "type": "string",
            "required": True,
            "empty": False,
        }
    })

    body = request.json
    response = body_validator.validate(body)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
    