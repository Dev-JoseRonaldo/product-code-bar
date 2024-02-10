from cerberus import Validator

body = {
    "data": {
    "elemento1": 123.98,
    "elemento2": "Ola Mundo",
    "elemento3": "123",
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "required": True,
        "schema": {
            "elemento1": {
                "type": "float",
                "required": True,
                "empty": False,
            },
            "elemento2": {
                "type": "string",
                "required": True,
                "empty": True,
            },
            "elemento3": {
                "type": "integer",
                "required": False,
                "empty": False,
            }
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(f'Erros: {body_validator.errors}')
else:
    print('Entrada Válida!')
