from typing import Any
from flask.views import MethodView

class Auth(MethodView):
    def __init__(self):
        super().__init__()
    
    def dispatch_request(self, **kwargs: Any):
        return super().dispatch_request(**kwargs)