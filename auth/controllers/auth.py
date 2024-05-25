from flask.views import MethodView
from requests import request

class Auth(MethodView):
    def __init__(self):
        super().__init__()
    
    def dispatch_request(self):
        
        return 'ok', 200