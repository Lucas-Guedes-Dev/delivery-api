from flasgger import swag_from

def get_docs():
    return swag_from({
        'tags': ['Auth'],
        'responses': {
            200: {
                'description': 'Success',
                'examples': {
                    'application/json': {'message': 'temos uma rota'}
                }
            }
        }
    })

def get_id_docs():
    return swag_from({
        'tags': ['Auth'],
        'parameters': [
            {
                'name': 'id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'The ID of the resource'
            }
        ],
        'responses': {
            200: {
                'description': 'Success',
                'examples': {
                    'application/json': {'message': 'chegou no get com id {id}'}
                }
            }
        }
    })

def post_docs():
    return swag_from({
        'tags': ['Auth'],
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'key': {
                            'type': 'string'
                        }
                    }
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Created',
                'examples': {
                    'application/json': {'message': 'POST request received', 'data': {}}
                }
            }
        }
    })

def patch_docs():
    return swag_from({
        'tags': ['Auth'],
        'parameters': [
            {
                'name': 'id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'The ID of the resource'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'key': {
                            'type': 'string'
                        }
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Success',
                'examples': {
                    'application/json': {'message': 'PATCH request received for ID {id}', 'data': {}}
                }
            },
            400: {
                'description': 'Bad Request',
                'examples': {
                    'application/json': {'error': 'ID is required for PATCH'}
                }
            }
        }
    })

def delete_docs():
    return swag_from({
        'tags': ['Auth'],
        'parameters': [
            {
                'name': 'id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'The ID of the resource'
            }
        ],
        'responses': {
            204: {
                'description': 'No Content',
                'examples': {
                    'application/json': {'message': 'DELETE request received for ID {id}'}
                }
            },
            400: {
                'description': 'Bad Request',
                'examples': {
                    'application/json': {'error': 'ID is required for DELETE'}
                }
            }
        }
    })
