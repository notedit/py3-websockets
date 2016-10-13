# -*- coding: utf-8 -*-

import jwt
import logging
import asyncio
import aiohttp

from collections import defaultdict
from aiohttp import web,WebSocketResponse




CHANNEL = 'dotEngine:websocket'


redis = yield from aioredis.create_redis(('localhost', 6379))

pub = yield from aioredis.create_redis(('localhost', 6379))

sub = yield from aioredis.create_redis(('localhost', 6379))



# use for publish  namespace  == appkey
# to is a room id
# data is json data
class WebsocketMessagePayload(object):

    def __init__(self,namespace=None,to=None,data=None):

        self.namespce = namespace
        self.to = to
        self.data = data


    def dict(self):

        return dict(namespace=self.namespace,
                    to=self.to,
                    data=self.data)



#  store connections and rooms
#  todo  move namespace to redis
class WebsocketStore(object):

    """
    connections:

    `
    {'uuid':websocket}
    `

    namespaces:

    `
    {
        'appkey1':{
            'room': set('uuid')
        },
        'appkey2':{}
    }
    `
    """

    def __init__(self):

        self.connections = dict()
        self.namespaces =  defaultdict(lambda : defaultdict(set))




async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    #  todo some auth with jwt
    #  set userid,room,appkey
    #  send peer_connected  and  peers  message



    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            pass

        elif msg.type == aiohttp.WSMsgType.ERROR:

            pass


    #  here  websocekt  closed

    #  send peer_removed message

    return ws




async def reader(ch):

    # redis subscribe
    pass


async def go():

    res = await sub.subscribe(CHANNEL)
    ch = res[0]

    #  redis sub



app = web.Application()
app.router.add_get('/ws', websocket_handler)
web.run_app(app)


