from telethon import events
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message
import asyncio
import os
import sys

@loader.tds
class TetrisAnimation(loader.Module):
	strings = {"name": "Tetris Animation"}


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
    await event.edit("⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n🟨🟨🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n🟨🟨🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n🟨🟨🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n💥💥💥💥⬛️⬛️⬛️ \n💥💥💥💥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
