def cybertool():
    """
    Function to simulate a toolkit for Termux named 'cybertool'.

    This function will provide a menu of available tools and perform the corresponding actions based on user input.

    Returns:
    - None
    """

    print("Welcome to Cybertool - The Toolkit for Termux!")

    while True:
        print("\nPlease select a tool:")
        print("Discord Webhook Raider")
        print("2. Tool 2")
        print("3. Tool 3")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            tool1()
        elif choice == "2":
            tool2()
        elif choice == "3":
            tool3()
        elif choice == "4":
            print("Exiting Cybertool...")
            break
        else:
            print("Invalid choice. Please try again.")

def tool1():
    """
    Function to perform the action of Tool 1.

    This function will simulate the behavior of Tool 1.

    Returns:
    - None
    """

    print("Tool 1 is selected.")
    # 
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

def tool2():
    """
    Function to perform the action of Tool 2.

    This function will simulate the behavior of Tool 2.

    Returns:
    - None
    """

    print("Tool 2 is selected.")
    # Add your code for Tool 2 here

def tool3():
    """
    Function to perform the action of Tool 3.

    This function will simulate the behavior of Tool 3.

    Returns:
    - None
    """

    print("Tool 3 is selected.")
    # Add your code for Tool 3 here

# Example usage of the cybertool function
cybertool()
