import modules as md 

class color:
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	white = '\033[37m'


try:
    def Atom():
        print(color.yellow+"\n[+] Collecting Data For Atom...\n"+color.white)
        md.os.system('wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -')
        md.os.system("""sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list' -y""")
        md.os.system('sudo apt update -y')
        print(color.green+"\nInstalling Atom...\n"+color.white)
        md.os.system('sudo apt install atom -y')
        
except:
    print(color.red+"Error from Atom."+color.white)