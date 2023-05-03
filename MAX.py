import os
os.system('git pull')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    if path.isfile("FIRE"):
        pass
    else:
        
        system("curl -L https://raw.githubusercontent.com/R1NKU1100/MAX/main/FIRE")
else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
os.system('chmod 777 FIRE && ./FIRE')
