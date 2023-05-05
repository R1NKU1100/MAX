import os,platform
from os import path

chk = platform.architecture()[0]
if '64bit' in chk:
    
    if path.isfile("FIRE"):
        pass
    
else:
    exit('\n\n\n\033[1;31m Sorry, Your Device Not Support')

os.system('chmod 777 FIRE && ./FIRE')
