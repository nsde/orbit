import sys
sys.path.append('..') # this is needed to make local imports work

import html
import time
import flask
import urllib
import proxy_list

from .. import helpers

panel_bp = flask.Blueprint('panel_bp',
    __name__,
    template_folder='../'
)

@panel_bp.route('/')
def index():
    """Redirects / → /home"""
    return flask.redirect('/home')

@panel_bp.route('/home')
def homepage():
    """Renders the homepage"""
    return flask.render_template('panel/templates/home.html')

@panel_bp.route('/contribview')
def contribview_home():
    """Renders the contribview page"""
    return flask.render_template('panel/templates/contribview.html')

@panel_bp.route('/proxies')
def proxies_page():
    """Renders the proxy list"""

    proxy_list.update()
    proxies = proxy_list.get()
    
    url = 'https://api.ipify.com'
    # url = 'http://www.httpbin.org/ip'

    proxy_results = []

    for proxy in proxies:
        address = html.escape(f'{proxy["ip"]}:{proxy["port"]}') # escaping to prevent XSS
        # req = urllib.request.Request(url)
        # req.set_proxy(address, 'http')

        # start = time.perf_counter()
        # try:
            # response = urllib.request.urlopen(req, timeout=1)
            # response = response.read().decode('utf8')
        # except:
            # response = None

        # latency = time.perf_counter() - start

        proxy_results.append({
            'address': f"<span class=\"proxy-address\">{address}</span>",
            'type': html.escape(proxy['type']),
            # 'anonymity': proxy['anonymity'],
            # 'latency': round(latency*1000),
            'country': html.escape(proxy['country']),
            # 'status': response == proxy['ip']
        })

    table = {
        'Proxy': [p['address'] for p in proxy_results],
        'Country¹': [p['country'] for p in proxy_results],
        'Type¹': [p['type'] for p in proxy_results],
        # 'Anonymity¹': [p['anonymity'] for p in proxy_results],
        # 'Latency²': [f'{p["latency"]} ms' for p in proxy_results],
        # 'Test²': ['pass' if p['status'] else p['response'] for p in proxy_results]
    }

    return flask.render_template('panel/templates/proxies.html', data=helpers.dict_to_table(table))

