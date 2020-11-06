
try:
    import os
    import time
    class color:
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        white = '\033[37m'


    try:
        def Code():
            os.system("sudo apt update -y")
            print(color.yellow+"\n[+] Collecting Data For VS Code...\n"+color.white)
            time.sleep(2)
            os.system("sudo apt install curl gpg software-properties-common apt-transport-https -y")
            os.system("curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -")
            os.system('echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" | sudo tee /etc/apt/sources.list.d/vscode.list')
            os.system("sudo apt update -y")
            print(color.green+"\nInstalling VS Code...\n"+color.yellow)
            os.system("sudo apt install code -y")

    except Exception as e:
                print(e)  

    except:
        print(color.red+"Error from vs_code."+color.white)
except Exception as e:
    print(e, "Raising erorr from vs_code")
