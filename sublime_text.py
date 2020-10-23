import modules as md 

class color:
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	white = '\033[37m'


try:
    def Sublime():
        print(color.yellow+"\n[+] Collecting Data For Sublime-Text...\n"+color.white)
        md.os.system("wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -")
        md.os.system("sudo apt-get install apt-transport-https -y")
        md.os.system('''echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list''')
        md.os.system("sudo apt update -y")
        print(color.green+"\nInstalling Sublime-Text...\n"+color.white)
        md.os.system("sudo apt install sublime-text -y")
    

except:
    print(color.red+"Error from Sublime"+color.white)