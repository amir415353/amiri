# Auto Visit (/visit)
# Chris Crypto Gaming & Financials
# Youtube Channel : http://bit.ly/CCGYTC
# E-mail : chriscryptogaming@gmail.com
# ETH Donations : 0xf410dCC5b41BF683390aCF0d6D2f0CCb198f3f86
# BTC Donations : 1C7SVC1mPBcXPYwq2jM765MKgQLm1S7DkY
# Doge Donations : DDn8sexiCcpi4MSCA1NPGz3G6vJLFRUKQj
# ZEC Donations : t1SgzYXhusasn7xaMzBhqE3Lfx4fBfrEFyF
# LTC Donations : ltc1qqwzdz03z6h5y5382lgvyhsuykzcrz580mj89u9
# BCH Donations : qqzjvgs0s2leev5gtam6cfm6fqch0kxw9q3narmjj4
# LTC Clickbot : http://bit.ly/35ME9Cq
# Doge Clickbot : http://bit.ly/35RO21J
# ZEC Clickbot : http://bit.ly/37WdN2L
# BTC Clickbot : http://bit.ly/2sAM1Zz
# BCH Clickbot : http://bit.ly/2R9GymM
# Support us on Brave! : http://bit.ly/CCGBrave

#Imports
import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events, errors
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# my.telegram.org values, get your own there
api_id = 1127509
api_hash = '7919be907884f1d388803b03f1994d78'

dogeclick_channel = 'freelite_coin_bot'

async def main():

	print(Fore.RED       + '       )  (    (    (              (        )  (               ) ')
	print(Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')
	print(Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')
	print(Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
	print(Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_)) __ ((_)(_)) (_(_())  ((_) ')
	print(Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
	print(Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
	print(Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
	print(Fore.BLUE   + '                      BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
	print(Fore.BLUE   + '                  YT Channel : http://bit.ly/CCGYTC  \n' + Fore.RESET)



	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +639162995600)\n')
		e = input('Press any key to exit...')
		exit(1)

	phone_number = sys.argv[1]

	if not os.path.exists("session"):
		os.mkdir("session")

	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()

	print(Fore.GREEN + f'Current account: {me.first_name}({me.username})\n' + Fore.RESET)
	print('Sending /Bonus command')

	# Start command /visit
	await client.send_message(dogeclick_channel, '💥 litecoin Bonus')
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		print(Fore.GREEN + f'{message}\n' + Fore.RESET)
	time.sleep(61)
	await client.send_message(dogeclick_channel, '💥 litecoin Bonus')

	await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(main())
