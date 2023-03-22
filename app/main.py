from aiohttp import web

from context import app_context
from middleware import session_middleware
from views import AdvertisementView, UserView


ads_site = web.Application()

ads_site.cleanup_ctx.append(app_context)
ads_site.middlewares.append(session_middleware)


ads_site.add_routes([
    web.get('/ads/{advertisement_id:\d+}', AdvertisementView),
    web.post('/ads', AdvertisementView),
    web.patch('/ads/{advertisement_id:\d+}', AdvertisementView),
    web.delete('/ads/{advertisement_id:\d+}', AdvertisementView),
    web.get('/users/{user_id:\d+}', UserView),
    web.post('/users', UserView),
    web.patch('/users/{user_id:\d+}', UserView),
    web.delete('/users/{user_id:\d+}', UserView)
])


if __name__ == '__main__':
    web.run_app(ads_site)