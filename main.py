import aiohttp
import asyncio
import sys
import os
import json
import random
from colorama import *
from pystyle import *

def clear():
  os.system("clear")

clear()


xeto = """▒▐▌▐▌░▐█▀▀▒█▀█▀█▒▐█▀▀█▌     ▒▄█▀▀█▒██▄░▒█▌░▐██▒▐█▀█░▐█▀▀
░▒▐▌░░▐█▀▀░░▒█░░▒▐█▄▒█▌     ▒▀▀█▄▄▒▐█▒█▒█░─░█▌▒▐█▄█░▐█▀▀
▒▐▌▐▌░▐█▄▄░▒▄█▄░▒▐██▄█▌     ▒█▄▄█▀▒██░▒██▌░▐██▒▐█░░░▐█▄▄


           > Press Enter

"""


os.system("mode 175,30 & title [Vanity Sniper - Xeto]")

Anime.Fade(Center.Center(xeto), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)

token = input("[>] Token: ")
bot = input("[>] Bot True/False: ")
guild = int(input("[>] Enter Guild ID To Add Sniped Vanity Code: "))
code = input("[>] Vanity Code To Snipe, discord.gg/: ")
randno = random.randint(10, 99)
api_ = [6,9,8]
api = random.choices(api_)

clear()

if bot in ["True", "true", True]:
  headers = {"Authorization": "Bot {}".format(token)}

elif bot in ["False", "false", False]:
  headers = {"Authorization": token}

async def snipe_vanity():
  nigger = {
    "code": code,
    "reason": f"KaramveerPlayZ-Sniper-{randno}"
  }
  async with aiohttp.ClientSession() as ssss:
    async with ssss.patch(f"https://discord.com/api/v9/guilds/{guild}/vanity-url", json=nigger, headers=headers) as bruh:
      if bruh.status in (200, 201, 204):
        sniped = """  ▒▐▌▐▌░▐█▀▀▒█▀█▀█▒▐█▀▀█▌     ▒▄█▀▀█▒██▄░▒█▌░▐██▒▐█▀█░▐█▀▀
░▒▐▌░░▐█▀▀░░▒█░░▒▐█▄▒█▌     ▒▀▀█▄▄▒▐█▒█▒█░─░█▌▒▐█▄█░▐█▀▀
▒▐▌▐▌░▐█▄▄░▒▄█▄░▒▐██▄█▌     ▒█▄▄█▀▒██░▒██▌░▐██▒▐█░░░▐█▄▄

      [+] Xeto | Vanity Sniped"""
        Anime.Fade(Center.Center(sniped), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)
        sys.exit()

async def check_vanity():
  async with aiohttp.ClientSession() as idk:
    while True:
      async with idk.get(f"https://discord.com/api/v9/invites/{code}", headers=headers) as gg:
        if gg.status == 404:
          await snipe_vanity()
        else:
          taken = f"[-] xeto| Vanity Is Taken, Still Trying To Snipe discord.gg/{code}."
        print(taken)
      


loop = asyncio.get_event_loop()
loop.run_until_complete(check_vanity())
