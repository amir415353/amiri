#Imports
import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# my.telegram.org values, get your own there
api_id = 1127509
api_hash = '7919be907884f1d388803b03f1994d78'
lines2 = []
# Date & Time Header
def print_msg_time(message):
	print('[' + Fore.YELLOW + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

#Personalized Message
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
		print('-> Input number in international format (example: +10123456789)\n')
		e = input('Press any key to exit...')
		exit(1)

	phone_number = sys.argv[1]

	if not os.path.exists("session"):
		os.mkdir("session")

	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()

	# Current account & username
	print(Fore.GREEN + f'               Current account: {me.first_name}({me.username})\n' + Fore.RESET)
	print_msg_time('leaving channels')
	async for message in client.iter_dialogs():
		message2 = message.id
		message3 = str(message2)
		if '-100' in message3:
			lines2.append(message2)
	for input_channel in lines2:
		await client.delete_dialog(input_channel)
		print_msg_time(f'{input_channel} has been leaved')
		time.sleep(2)
asyncio.get_event_loop().run_until_complete(main())
