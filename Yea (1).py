import time, random
from .. import loader, utils

def register(cb):
	cb(YeaMod())
	
class YeaMod(loader.Module):
   strings = {'name': 'Yea'}
   def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
              
   async def yeacmd(self, message):
      num = 0
      while num != 11:
         yea = '''
ㅤㅤㅤ  🔺
ㅤ ㅤ🔻🟥🔻 
ㅤ❄️  🟩🟩    ❄️
ㅤ ㅤ🟩@🟩
❄️ 🟩@🟩@
ㅤㅤ 🟩@🟩    ❄️
❄️ 🟩@🟩@
ㅤ@🟩@🟩@ ❄️
 🟩@🟩@🟩@
ㅤㅤㅤ  🟫
ㅤㅤㅤ  🟫ㅤㅤㅤ  
  Happy new year!
'''
         yeaall = ''
         for i in yea:
            if i == "@":
               yeaall += random.choice(["🟥", "🟧", "🟦", "🟪", "🟩", "🟩"])
            else:
               yeaall += i
         await message.edit(yeaall)
         time.sleep(0.5)
         num += 1
