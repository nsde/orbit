import sys
sys.path.append('..') # this is needed to make local imports work

import flask
import requests

from .. import helpers

api_bp = flask.Blueprint('api_bp', __name__)

@api_bp.route('/contribview/<user>/<repo>')
def contribview(user, repo):
    title = f'{user}/{repo}'
    
    api_url = f'https://api.github.com/repos/{user}/{repo}/contributors'
    response = requests.get(api_url).json()

    if not isinstance(response, list):
        return flask.abort(404, 'Repository not found. Please check the URL.')

    users = []

    for count, user in enumerate(response, start=1):
        if '[bot]' in user.get('login'):
            continue

        emoji = ''

        if len(response) >= 6:
            if count == 1:
                emoji = '🥇'
            if count == 2:
                emoji = '🥈'
            if count == 3:
                emoji = '🥉'
        elif len(response) >= 3:
            if count == 1:
                emoji = '🎖️'

        users.append({
            'name': user.get('login') or 'ghost',
            'icon': helpers.base64_source(user.get('avatar_url') + '&s=64'),
            'commits': user.get('contributions'),
            'emoji': emoji
        })

    css = helpers.get_css(['inter', 'orbitium', 'space'])
    rendered_html = flask.render_template('api/templates/contribview.html', css=css, user=user, repo=repo, title=title, users=users)
    
    resp = flask.Response(rendered_html)
    resp.headers['Content-Type'] = 'image/svg+xml'

    return resp
