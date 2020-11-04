#!/usr/bin/bash/

from files import all_modules as md
from files.Text_Editors import 	(	
									atom, 
									vs_code, 
									sublime_text, 
									pycharm
								)
from files.Browsers import (
								tor,
								chrome
							)					

class color:
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	white = '\033[37m'

def update():
	try:
		print(color.green+"Running: sudo apt update...")
		md.os.system("sudo apt update -y")
		user = input("Do you want to upgrade? (y/n): ")
		if user.lower()=="y":
			print(color.green+"\n[+] Starting Upgrade...\n")
			md.time.sleep(1)
			os.system("sudo apt upgrade -y")
		else:
			print(color.red+"\nExiting...\n"+color.white)
			exit()
	except Exception as e:
		print(color.red + str(e) + color.white)

class Installation:
	def ide(self):
		try:	
			print("It may takes a bit of time. Please wait...")
			
			# calling and installing vscode
			VSCODE = vs_code.Code()
			print(VSCODE)

			# calling and installing sublime-text
			SublimeText = sublime_text.Sublime()
			print(SublimeText)

			# calling and installing atom
			ATOM = atom.Atom()
			print(ATOM)

			# calling and installing pycharm
			PYCHARM = pycharm.PyCharm()
			print(PYCHARM)

		except Exception as e:
			print(e)	
		
	def browser(self):
		try:
			print(color.green+"\nIt may takes a bit of time. Keep patience.\n")
			md.time.sleep(1)

			# installing chrome
			CHROME= chrome.ChromeBrowser() 
			print(CHROME)

			# installing tor
			TOR = tor.TorBrowser()
			print(TOR)
		
		except Exception as e:
			print(color.red+"\n{}\n".format(e))


	
	
if __name__ == "__main__":
	
	pip_install = input(color.green+"Do you have pip installed?\nIf not, it will download pip. (y/n): ")
	if pip_install.lower() == "y":
		pass
	else:
		md.os.system("sudo apt install python3-pip")

	md.time.sleep(1)
	update()
	md.time.sleep(1)
	print(color.green+"""

		\tChoose to Install
	----------------------------------------------------------------
	1. IDE (VS Code, Sublime Text, Atom, PyCharm)
	2. Browser (Chrome, Tor)
	3. All
	4. Exit
	
	""")
	
	option = int(input("Your Choise: "))
	if option == 1:
		print("""
				Text Editors
			--------------------------
			[+] VS Code
			[+] Sublime Text
			[+] Atom
			[+] PyCharm

			""")
		IDE = Installation()
		IDE.ide()
	elif option == 2:
		print("""
					Browser
			--------------------------
			[+] Chrome
			[+] Tor

			""")
		BROWSER = Installation()
		BROWSER.browser()
	elif option == 3:
		ALL = Installation()
		ALL.ide()
		ALL.browser()
	else:
		exit()




