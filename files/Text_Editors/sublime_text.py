
try:
    import os

    class color:
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        white = '\033[37m'

    try:
        def Sublime():
            print(color.yellow+"\n[+] Collecting Data For Sublime-Text...\n"+color.white)
            os.system("wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -")
            os.system("sudo apt-get install apt-transport-https -y")
            os.system('''echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list''')
            os.system("sudo apt update -y")
            print(color.green+"\nInstalling Sublime-Text...\n"+color.white)
            os.system("sudo apt install sublime-text -y")
        
    except:
        print(color.red+"Error from Sublime"+color.white)
except Exception as e:
    print(e, "Raising error from sublime-text...")