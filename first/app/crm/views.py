import uuid

from app.crm.models import User
from app.web.app import View

from aiohttp.web_response import json_response

class AddUserView(View):
    async def post(self):
        #self.request.app.database
        data = await self.request.json()
        user = User(email=data['email'], _id=uuid.uuid4())
        return json_response()
