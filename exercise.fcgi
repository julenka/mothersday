#!/home1/notjulie/venv/flask_hello_world/bin/python
from flup.server.fcgi import WSGIServer
from mothersday_app import app as application

WSGIServer(application).run()
