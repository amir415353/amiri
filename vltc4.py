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
import random
import requests
from requests.auth import HTTPProxyAuth
logging.basicConfig(level=logging.ERROR)

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup

color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# my.telegram.org values, get your own there
api_id = 1127509
api_hash = '7919be907884f1d388803b03f1994d78'

dogeclick_channel = 'Litecoin_click_bot'
def maini(url1):
	session = requests.Session()
	headers1 = {'Host': 'doge.click',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
	'Connection': 'keep-alive',
	'TE': 'Trailers'}
	url3 = 'https://doge.click/reward'
	headers2 = {'Host': 'scdn.dogeclick.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Connection': 'keep-alive',
	'Referer': url1}
	g = re.findall(r'http://doge.click/visit+\b/\w+', url1)
	f = str(g)
	c = f.replace("['http://doge.click/visit/", '')
	c = c.replace("'", '')
	c = c.replace(']', '')
	if True:
		try:
			amir = session.get(url1, headers=headers1)
			mir = amir.text
			if True:
				e1 = re.findall(r'''data-token="+[\w]+"''', mir)
				e2 = re.findall(r'''data-timer="[\d]+"''', mir)
				f1 = str(e1)
				f2 = str(e2)
				if '[]' not in f:
					d = f1.replace('''['data-token=''', '')
					d = d.replace('"', '')
					d = d.replace("'", '')
					d = d.replace("data-token=", '')
					d = d.replace('[', '')
					d = d.replace(']', '')
					d2 = re.search(r'[\d][\d]', f2).group()
					t = int(d2) + 2
					while t:
						mins, secs = divmod(t, 60)
						timeformat = '{:02d}:{:02d}'.format(mins, secs)
						print(timeformat, end='\r')
						time.sleep(1)
						t -= 1
					print('Done!')
					data = {"code": c,
					"token": d
					}
					x = requests.post(url3, headers=headers1, data=data)
					return
				elif '[]' in f:
					t = 12
					while t:
						mins, secs = divmod(t, 60)
						timeformat = '{:02d}:{:02d}'.format(mins, secs)
						print(timeformat, end='\r')
						time.sleep(1)
						t -= 1
					print('Done!')
					return
		except (requests.exceptions.TooManyRedirects, requests.exceptions.ConnectionError, requests.exceptions.ProxyError):
			maini(url1)

# Date & Time Header
def print_msg_time(message):
	print('[' + Fore.YELLOW + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')


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
	print_msg_time('Sending /visit command')

	# Start command /visit
	await client.send_message(dogeclick_channel, '/visit')

	# Start visiting the ads
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def visit_ads(event):
		try:
			url1 = event.original_update.message.reply_markup.rows[0].buttons[0].url
			print_msg_time('Visiting Website...Verifying Timer...')
			maini(url1)
		except AttributeError:
			pass
	# Print earned money
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:
			print_msg_time(Fore.GREEN + f'{message}\n' + Fore.RESET)

	# No more ads
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:
			print_msg_time(Fore.RED + 'Sorry, there are no new ads available\n' + Fore.RESET)


	# Balance Information
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def balance(event):
		message = event.raw_text
		if 'Sorry, there are no new ads available' in message:
			await client.send_message(dogeclick_channel, '/balance')
		if 'Available balance:' in message:
			print_msg_time(Fore.GREEN + f'{message}\n' + Fore.RESET)



			exit(1)


	await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(main())
