from urllib.request import Request
from aiohttp.web import Application as AiohttpApplication, run_app as aiohttp_run_app, View as AiohttpView
from aiohttp.web import Request as AiohttpRequest
#from web.routes import setup_routes
#from routes import setup_routes
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    database: dict = {}
    
class Request(AiohttpRequest):
    @property
    def app(self) -> "Application":
        return super().app()
           

class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request

    
app = Application()


def run_app():
    #app.database
    setup_routes(app)
    aiohttp_run_app(app)

