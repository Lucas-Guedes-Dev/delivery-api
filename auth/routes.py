from flask import current_app as app
from auth.view.auth import Auth

app.add_url_rule('/', view_func=Auth.as_view('index'))
app.add_url_rule('/paraprara', view_func=Auth.as_view('view'))