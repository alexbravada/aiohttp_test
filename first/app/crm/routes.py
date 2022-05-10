from aiohttp.web_app import Application
from first.app.crm.views import index

def setup_routes(app: Application):
    app.router.add_get('/index', index)