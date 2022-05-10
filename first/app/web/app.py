from aiohttp.web import Application, run_app as aiohttp_run_app
#from web.routes import setup_routes
#from routes import setup_routes
from app.web.routes import setup_routes

app = Application()


def run_app():
    setup_routes(app)
    aiohttp_run_app(app)
