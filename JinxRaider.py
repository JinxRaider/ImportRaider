import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import os
import time
from colorama import Fore, Back, Style
from discord_webhook import DiscordWebhook
import sys


os.system('clear')
print(Fore.GREEN + ' ')
time.sleep(0.5)
print("""
      _  _____  ______   _    _                   
     | |  | |  | |  \ \ \ \  / /                  
 _   | |  | |  | |  | |  >|--|<                   
|_|__|_| _|_|_ |_|  |_| /_/  \_\                  
                                                  
 ______   ______  _____  _____    ______  ______  
| |  | \ | |  | |  | |  | | \ \  | |     | |  | \ 
| |__| | | |__| |  | |  | |  | | | |---- | |__| | 
|_|  \_\ |_|  |_| _|_|_ |_|_/_/  |_|____ |_|  \_\ 
                                                  """)
print("")
print("")
print("")
print("")
print(Fore.GREEN + ' _____________________________________________________')
print(Fore.GREEN + '| Discord webhook spammer: 1 | SOON: 2|')
print(Fore.GREEN + ' ____________________________________________________')
print("")
print("")
print(Style.RESET_ALL)
option = input("Option: ")

if option == "1":
	rusurewebhook = input("are you sure? it cannot be stopped unless the webhook is deleted y/n: ")
	if rusurewebhook == "y":
		weburl =  input("webhook url: ")
		msg =  input("message: ")
		def whspam():
			webhook = DiscordWebhook(url= weburl, content= msg)
			response = webhook.execute()
	else:
		print("stopped/incorrect answer")

elif option == "2":
	print("W.I.P")

else:
	print("invalid option!")
	time.sleep(1)
	os.execv(sys.argv[0], sys.argv)

while True:
	whspam()
