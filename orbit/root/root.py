import sys
sys.path.append('..') # this is needed to make local imports work

import flask

from .. import helpers

root_bp = flask.Blueprint('root_bp',
    __name__,
    template_folder='../'
)

sidebar_paths = [i['path'] for i in helpers.get_sidenav() if isinstance(i, dict) and not '#' in i['path']]

@root_bp.route('/<page>/↑')
def move_up(page):
    """Moves up in the sidebar when ALT+↑ are pressed."""
    return flask.redirect('/' + sidebar_paths[sidebar_paths.index(page)-1])

@root_bp.route('/<page>/↓')
def move_down(page):
    """Moves down in the sidebar when ALT+↓ are pressed."""
    return flask.redirect('/' + sidebar_paths[sidebar_paths.index(page)+1])

@root_bp.route('/redirect/to/<path:subpath>')
def redirect_to(subpath):
    """Redirect endpoint. This is needed for the external nav-items in the sidebar."""
    return flask.redirect(subpath.replace(':/', '://'))
