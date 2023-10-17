import os
import time
import sys
from colorama import Fore, Back, Style
from discord_webhook import DiscordWebhook

def clear():
	os.system('clear')

clear()
print(Fore.GREEN + ' ')
time.sleep(0.5)
os.system('toilet J')
time.sleep(2)
clear()
os.system('toilet Ji')
time.sleep(2)
clear()
os.system('toilet Jin')
time.sleep(2)
clear()
os.system('toilet Jinx')
time.sleep(2)
os.system('toilet R')
time.sleep(2)
clear()
os.system('toilet Jinx')
os.system('toilet Ra')
time.sleep(2)
clear()
os.system('toilet Jinx')
os.system('toilet Rai')
time.sleep(2)
clear()
os.system('toilet Jinx')
os.system('toilet Raid')
time.sleep(2)
clear()
os.system('toilet Jinx')
os.system('toilet Raide')
time.sleep(2)
clear()
os.system('toilet Jinx')
os.system('toilet Raider')


print("")
print("")
print("")
print("")
print(Fore.GREEN + ' _____________________________________________________')
print(Fore.GREEN + '| Discord webhook spammer: 1 | SOON: 2')
print(Fore.GREEN + ' ____________________________________________________')
print(Fore.GREEN + '| Quit: 3                    | Soon: 4 |')
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
		while True:
			whspam()
	else:
		print("stopped/incorrect answer")

elif option == "2":
	print("W.I.P")

else:
	print("invalid option!")
	time.sleep(1)