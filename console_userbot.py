from aiohttp import web
from pyrogram import Client
import asyncio

app = Client("userbot", api_id=123456, api_hash="abcd1234")
routes = web.RouteTableDef()

@routes.post("/webhook")
async def webhook_handler(request):
    data = await request.json()
    print("Webhook data:", data)
    return web.Response(text="ok")

async def main():
    await app.start()
    runner = web.AppRunner(web.Application().add_routes(routes))
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    await asyncio.Event().wait()

asyncio.run(main())
