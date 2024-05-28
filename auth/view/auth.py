from flask.views import MethodView
from flask import jsonify, request

class Auth(MethodView):
    def __init__(self):
        super().__init__()
    
    def dispatch_request(self):
        if request.method == "POST":
            pass
        elif request.method == 'GET':
            pass
        
        return jsonify({'ok': 'ok'}), 200