import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message


@loader.tds
class FarmIrisMod(loader.Module):
    """Для автоматического фарминга коинов в ирисботе"""

    strings = {
        "name": "tbio",
        "tbion": "<i>✅Отложенка создана, автосмена запущена, всё начнётся через 20 секунд...</i>",
        "tbio_already": "<i>Уже запущено</i>",
        "tbif": "<i>❌Автосмена остановлена.\n☢️Надюпано:</i> <b>%coins% i¢</b>",
         }

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.myid = (await client.get_me()).id
        self.iris = 2109543251

    async def tbioncmd(self, message):
        """Запустить автосмену"""
        status = self.db.get(self.name, "status", False)
        if status:
            return await message.edit(self.strings["tbio_already"])
        self.db.set(self.name, "status", True)
        await self.client.send_message(
            self.iris, ".bio random(👦 @KruzProjects - проекты от меня. 💼 Реклама - @KruzAd, 👦 @KruzProjects - проекты от меня. 💼 Помощь - @KruziX)", schedule=timedelta(seconds=20)
        )
        await message.edit(self.strings["tbion"])

    async def tbifcmd(self, message):
        """Остановить автосмену"""
        self.db.set(self.name, "status", False)
        
    async def tbiocmd(self, message):
        """Смена био снова запущена?"""
        
    async def watcher(self, event):
        if not isinstance(event, Message):
            return
        chat = utils.get_chat_id(event)
        if chat != self.iris:
            return
        status = self.db.get(self.name, "status", False)
        if not status:
            return
        if event.raw_text == ".bio random(👦 @KruzProjects - проекты от меня. 💼 Реклама - @KruzAd, 👦 @KruzProjects - проекты от меня. 💼 Помощь - @KruziX)"
                   return await self.client.send_message(
                self.iris, ".bio random(👦 @KruzProjects - проекты от меня. 💼 Реклама - @KruzAd, 👦 @KruzProjects - проекты от меня. 💼 Помощь - @KruziX)", schedule=timedelta(minutes=random.randint(1, 20))
            )
        if event.sender_id != self.iris:
            return
        if "НЕЗАЧЁТ!" in event.raw_text:
            args = [int(x) for x in event.raw_text.split() if x.isnumeric()]
            randelta = random.randint(20, 60)
            if len(args) == 4:
                delta = timedelta(
                    hours=args[1], minutes=args[2], seconds=args[3] + randelta
                )
            elif len(args) == 3:
                delta = timedelta(minutes=args[1], seconds=args[2] + randelta)
            elif len(args) == 2:
                delta = timedelta(seconds=args[1] + randelta)
            else:
                return
            sch = (
                await self.client(
                    functions.messages.GetScheduledHistoryRequest(self.iris, 1488)
                )
            ).messages
            await self.client(
                functions.messages.DeleteScheduledMessagesRequest(
                    self.iris, id=[x.id for x in sch]
                )
            )
            return await self.client.send_message(self.iris, ".bio random(👦 @KruzProjects - проекты от меня. 💼 Реклама - @KruzAd, 👦 @KruzProjects - проекты от меня. 💼 Помощь - @KruziX)", schedule=delta)
