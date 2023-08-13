import os,platform
os.system('git pull') 
bit=platform.architecture()[0]
if bit=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif bit=="64bit":
     __import__("Cyber")
 
