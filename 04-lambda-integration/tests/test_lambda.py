import json
from lambdas.lambda_handler import handler


def event(resource: str, httpMethod: str, body: any = {}, path_params: dict = {}) -> dict:
    return {
        'resource': resource,
        'httpMethod': httpMethod,
        'body': json.dumps(body),
        'pathParameters': path_params
    }


def context() -> dict:
    return {}


def test_method_not_supported():
    assert handler(event('', ''), context()) == {'statusCode': 404, 'body': '"Method not supported"'}


def test_get_heroes():
    assert handler(event('/heroes', 'GET'), context()) == {'statusCode': 200, 'body': '[{"id": 1, "name": "superman"}, {"id": 2, "name": "batman"}]'}


def test_get_hero_by_id():
    assert handler(event('/heroes/{id}', 'GET', path_params={'id': '1'}), context()) == {'statusCode': 200, 'body': '{"id": 1, "name": "superman"}'}
    assert handler(event('/heroes/{id}', 'GET', path_params={'id': '2'}), context()) == {'statusCode': 200, 'body': '{"id": 2, "name": "batman"}'}

