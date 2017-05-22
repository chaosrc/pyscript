#!/usr/bin/python3


import pexpect
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 4e2f2089eb702a5f2bd68be1e5e20235aea7388d
import time

name='root'
ip='45.78.22.110'
port='29794'
password='8r8eUN4LG9TR'
<<<<<<< HEAD
=======
=======
import sys

name='root'
ip='43.77.52.112'
port='22'
password='8r8UN4G9RF7KG'
>>>>>>> 6e9414c82c588fc1226801b2263b1f492b9c6973
>>>>>>> 4e2f2089eb702a5f2bd68be1e5e20235aea7388d

cmd='ssh -f -N -D 7070 %s@%s -p %s'%(name,ip,port)

#if len(sys.argv)>1:
#    pass

def conssh(cmd):

    try:
        result=pexpect.spawn(cmd)
        i=result.expect(['password:','continue connecting (yes/no)?'],timeout=60)
        
        if i==1:
            result.sendline('yes')
            result.expect('password:',timeout=20)
<<<<<<< HEAD
        print(result.after.decode('utf-8')+'*'*6)	
        result.sendline(password)
=======
<<<<<<< HEAD
        print(result.after.decode('utf-8')+'*'*6)	
        result.sendline(password)
=======
        print(result.before.decode('utf-8'))
        print(result.after.decode('utf-8')+'*'*6)	
        result.sendline(password)
        
>>>>>>> 6e9414c82c588fc1226801b2263b1f492b9c6973
>>>>>>> 4e2f2089eb702a5f2bd68be1e5e20235aea7388d
        #result.expect('root@',timeout=20)
        #result.sendline('ls /')
        #result.expect(['bin','mnt','sys'],timeout=20)
        #print(result.readline().decode('ascii'))
        #result.sendline('exit')
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
        
>>>>>>> 6e9414c82c588fc1226801b2263b1f492b9c6973
>>>>>>> 4e2f2089eb702a5f2bd68be1e5e20235aea7388d
        print('seccuss')
        result.wait()
    except pexpect.EOF:
        print('EOF')
        result.close()
    except pexpect.TIMEOUT:
        print('timeout')
        result.close()
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 4e2f2089eb702a5f2bd68be1e5e20235aea7388d


if __name__ =='__main__':
    conssh(cmd)
    
<<<<<<< HEAD
=======
=======
        
        
if __name__ =='__main__':
    conssh(cmd1)
>>>>>>> 6e9414c82c588fc1226801b2263b1f492b9c6973

>>>>>>> 4e2f2089eb702a5f2bd68be1e5e20235aea7388d

