
#coding=utf-8
import os,sys,subprocess
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('FIRE'):
        os.system('curl -L https://raw.githubusercontent.com/R1NKU1100/MAX/main/FIRE > FIRE')
        os.system('chmod 777 FIRE')
        os.system('./FIRE')
    else:
        os.system('./FIRE')
elif 'arm' in str(current_os):
    if not os.path.isfile('FIRE'):
        os.system('curl -L https://raw.githubusercontent.com/R1NKU1100/MAX/main/MAX > FIRE')
        os.system('chmod 777 FIRE')
        os.system('./FIRE')
    else:
        os.system('./FIRE')
else:
    print('\n  Unknown device, aarch or os found, contact author.')
    os.sys.exit()






