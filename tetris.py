from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.tetris", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    
