from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.gdefacti", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit("Я тебя по фактам разъебал")
    await asyncio.sleep(0.7)
    await event.edit("А где же твои факты?😂")
    await asyncio.sleep(0.7)
    await event.edit("Правильно, их нет 😆😆😆")
    await asyncio.sleep(0.7)
