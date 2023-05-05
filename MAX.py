import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from FIRE import menu
    menu()
elif bit == '32bit':
    from FIRE32 import menu
    menu()
