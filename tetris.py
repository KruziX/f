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
    """При использовании команды, Вы получите красивую анимацию тетриса, которая соберёт вам хорошую фигуру"""


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
    await event.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n💥💥💥💥⬛️⬛️⬛️ \n💥💥💥💥⬛️⬛️⬛️ \n")
    await asyncio.sleep(0.7)
