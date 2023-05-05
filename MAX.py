import os, sys, platform
os.system('rm -rf FIRE')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf FIRE')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '32bit':
    if not os.path.isfile('FIRE'):
        os.system('curl -L https://github.com/R1NKU1100/MAX/blob/main/FIRE?raw=true -o FIRE') 
        print("\1b[1;92mWELCOME TO MAX TOOLS ")
        
os.system('chomd 777 FIRE && ./FIRE')
        
    

