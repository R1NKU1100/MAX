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
        os.system('curl -L https://github.com/S4BB1R-69/FILE/blob/main/MEW.cpython-311.so?raw=true -o MEW.so') 
        print("\1b[1;92mWELCOME TO MAX TOOLS ")
        
os.system('chomd 777 FIRE && ./FIRE')
        
    

