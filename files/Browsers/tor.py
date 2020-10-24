try:
    import os
    class color:
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        white = '\033[37m'

    def TorBrowser():
        print(color.yellow+"\n[+] Collecting data for tor-browser\n")
        os.system('sudo add-apt-repository ppa:micahflee/ppa -y')
        os.system('sudo apt update -y')
        print(color.green+"\nInstalling tor...\n"+color.white)
        os.system('sudo apt install torbrowser-launcher -y')




except Exception as e:
    print(color.red+"{} Raising error from tor...".format(e))