
try:
    import os

    class color:
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        white = '\033[37m'

    def Atom():
        os.system('sudo apt update -y')
        print(color.yellow+"\n[+] Collecting Data For Atom...\n"+color.white)
        os.system('wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -')
        os.system("""sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list' -y""")
        os.system('sudo apt update -y')
        print(color.green+"\nInstalling Atom...\n"+color.white)
        os.system('sudo apt install atom -y')
    
except Exception as e:
    print(e, "Raising error from atom...")
