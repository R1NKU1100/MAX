import os, sys, platform
os.system('rm -rf FIRE')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf FIRE')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':

os.system('chmod 777 FIRE && ./FIRE')
        
    

