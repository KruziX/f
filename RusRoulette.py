#by @CREATIVE_tg1

from .. import loader
import random
from asyncio import sleep

@loader.tds
class RussianRouletteMod(loader.Module):
	strings = {"name": "RusRoulette"}
	@loader.owner
	
	async def roulettecmd(self, message):
		"""Используй .roulette чтобы сыграть в русскую рулетку.  by @CREATIVE_tg1"""
		ammo = ("<b>Вы лох сударь.</b>", "<b>Вы проиграли!</b>", "<b>Начинай заново, твои мозги разлетелись по всей стене.</b>", "<b>Пам, пам, пам, у нас труп.</b>", "<b>Ты выиграл!</b>", "<b>Ты выжил, но больше не играй, тебя ждут близкие люди!</b>", "<b>Ты умер(нет).</b>", "<b>Тебе очень повезло, ибо следующий патрон был не холостым.</b>")

		number = random.choice(ammo)
		
		await message.edit("<b>*Выстрел*</b>")
		await sleep(1)
		
		await message.edit("⭕⭕⭕")
		await sleep(2)			
		await message.edit(number)
