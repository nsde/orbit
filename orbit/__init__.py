import os

import flask

from dotenv import load_dotenv

from . import helpers

UPLOAD_LIMIT_MB = 1024

load_dotenv()

def create_app():
    """Prepares the flask.Flask web server"""

    app = flask.Flask(__name__)
    app.secret_key = os.getenv('FLASK_SECRET_KEY')

    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    app.config['MAX_CONTENT_LENGTH'] = UPLOAD_LIMIT_MB * 1024 * 1024

    from orbit.api.api import api_bp
    from orbit.root.root import root_bp
    from orbit.panel.panel import panel_bp

    app.register_blueprint(api_bp, url_prefix='/')
    app.register_blueprint(root_bp, url_prefix='/')
    app.register_blueprint(panel_bp, url_prefix='/')

    @app.context_processor
    def inject_sidebar():
        """Injects the following variables directly into every single website rendered:"""

        return dict(
            navigation=helpers.get_sidenav(),
            is_sidebar_closed=flask.request.cookies.get('sidebar') == 'closed',
        )

    return app
