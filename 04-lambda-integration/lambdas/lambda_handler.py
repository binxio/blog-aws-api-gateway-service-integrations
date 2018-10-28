import json

def response(status_code: int, body: any) -> dict:
    return {
        'statusCode': status_code,
        'body': json.dumps(body)
    }

def handler(event, context):
    resource = event['resource']
    method = event['httpMethod']

    heroes = [{'id': 1, 'name': 'superman'}, {'id': 2, 'name': 'batman'}]

    if resource == '/heroes':
        if method == 'GET':
            return response(200, heroes)
        elif method == 'POST':
            return response(200, json.loads(event['body']))

    elif resource == '/heroes/{id}':
        id = event['pathParameters']['id']
        hero_by_id = [h for h in heroes if h['id'] == int(id)]
        if method == 'GET':
            if len(hero_by_id) != 0:
                return response(200, hero_by_id[0])
            else:
                return response(404, 'Not Found')
        elif method == 'DELETE':
            if len(hero_by_id) != 0:
                return response(200, hero_by_id[0])
            else:
                return response(404, 'Not Found')
        else:
            return response(404, 'Method not supported')

    elif resource == '/search/{name}':
        name = event['pathParameters']['name']
        if method == 'GET':
            return response(200, [h for h in heroes if h['name'] == name])
        else:
            return response(404, 'Method not supported')
    else:
        return response(404, 'Method not supported')