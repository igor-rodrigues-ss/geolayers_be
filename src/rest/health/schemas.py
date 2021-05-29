from src.config import UP, DOWN


health_check = {
    'status': f'{UP} | {DOWN}',
    'checks': [
        {
            'name': 'str',
            'status': f'{UP} | {DOWN}',
            '?msg': 'str'
        }
    ]
}

list_services = [
    'service_name'
]

service_detail = {}
