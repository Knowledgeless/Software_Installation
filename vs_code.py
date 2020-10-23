import modules as md 

class color:
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	white = '\033[37m'


try:
    def Code():
        print(color.yellow+"\n[+] Collecting Data For VS Code...\n"+color.white)
        md.time.sleep(2)
        md.os.system("sudo apt install software-properties-common apt-transport-https wget -y")
        md.os.system("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
        md.os.system('sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main -y"')
        md.os.system("sudo apt update -y")
        print(color.green+"\nInstalling VS Code...\n"+color.yellow)
        md.os.system("sudo apt install code -y")
        

except Exception as e:
			print(e)  

except:
    print(color.red+"Error from vs_code."+color.white)

