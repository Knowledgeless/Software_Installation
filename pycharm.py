import modules as md 

class color:
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	white = '\033[37m'


try: 
    def PyCharm():
        md.os.system("sudo apt install snapd -y")
        md.os.system("sudo systemctl unmask snapd.service")
        md.os.system("systemctl enable snapd.service")
        md.os.system("systemctl start snapd.service")
        print(color.green+"Installing PyCharm..."+color.white)
        md.os.system("sudo snap install pycharm-community --classic")

except:
    print(color.red+"Error from PyCharm."+color.white)

PyCharm()