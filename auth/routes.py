from flask import current_app as app
from auth.controllers.auth import Auth

app.add_url_rule('/', view_func=Auth.as_view('index'))
