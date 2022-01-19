from flask import Flask

from . import routes
from . import routes

def create_app():
    app = Flask(__name__)

    app.register_blueprint(routes.bp)

    @app.after_request
    def universal_header(resp):
        resp.headers["X-Research"] = "AP Research"
        return resp
    return app