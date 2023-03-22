from aiohttp import web 
from bcrypt import hashpw, gensalt

from crud import get_object, create_object, patch_object, delete_object
from models import Advertisement, User


class AdvertisementView(web.View):

    async def get(self):
        advertisement = await get_object(int(self.request.match_info['advertisement_id']), Advertisement, self.request['session'])
        return web.json_response({
            'id': advertisement.id,
            'owner': advertisement.owner_id,
            'title': advertisement.title,
            'description': advertisement.description,
            'created at': int(advertisement.created_at.timestamp())
        })
    
    async def post(self): 
        json_data = await self.request.json()
        new_advertisemet = await create_object(Advertisement, self.request['session'], **json_data)
        return web.json_response({'id': new_advertisemet.id})

    async def patch(self):
        advertisement = await get_object(int(self.request.match_info['advertisement_id']), Advertisement, self.request['session'])
        json_data = await self.request.json()
        await patch_object(advertisement, self.request['session'], **json_data)
        return web.json_response({'status': 'succesfully patched'})

    async def delete(self):
        advertisement = await get_object(int(self.request.match_info['advertisement_id']), Advertisement, self.request['session'])
        await delete_object(advertisement, self.request['session'])
        return web.json_response({'status': 'successfully deleted'})
    

class UserView(web.View):

    async def get(self):
        user = await get_object(int(self.request.match_info['user_id']), User, self.request['session'])
        return web.json_response({
            'id': user.id,
            'email': user.email
        })

    async def post(self): 
        json_data = await self.request.json()
        json_data['password'] = hashpw(json_data['password'].encode(), salt=gensalt()).decode()
        new_user = await create_object(User, self.request['session'], **json_data)

        return web.json_response({'id': new_user.id})

    async def patch(self):
        user = await get_object(int(self.request.match_info['user_id']), User, self.request['session'])
        json_data = await self.request.json()
        await patch_object(user, self.request['session'], **json_data)
        return web.json_response({'status': 'succesfully patched'})

    async def delete(self):
        user = await get_object(int(self.request.match_info['user_id']), User, self.request['session'])
        await delete_object(user, self.request['session'])
        return web.json_response({'status': 'successfully deleted'})