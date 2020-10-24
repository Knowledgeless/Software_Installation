try:
    import os
    import time 

    class color:
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        white = '\033[37m'

    def ChromeBrowser():
        print(color.yellow + "\n[+] Collecting data for chrome...\n")
        os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        print(color.green+"\nInstalling chrome...\n"+color.white)
        os.system('sudo apt install ./google-chrome-stable_current_amd64.deb -y')

except Exception as e:
    print(color.red+ "{} Raising error from chrome...".format(e))