
try:
    import os

    class color:
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        white = '\033[37m'

    try: 
        def PyCharm():
            os.system('sudo apt update -y')
            os.system("sudo apt install snapd -y")
            os.system("sudo systemctl unmask snapd.service")
            os.system("systemctl enable snapd.service")
            os.system("systemctl start snapd.service")
            print(color.green+"Installing PyCharm..."+color.white)
            os.system("sudo snap install pycharm-community --classic")
            
    except:
        print(color.red+"Error from PyCharm."+color.white)

except Exception as e:
    print(e, "Raising error from pycharm...")
