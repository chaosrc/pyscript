#!/usr/bin/python3


import pexpect
import sys

name='root'
ip='43.77.52.112'
port='22'
password='8r8UN4G9RF7KG'

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
        print(result.before.decode('utf-8'))
        print(result.after.decode('utf-8')+'*'*6)	
        result.sendline(password)
        
        #result.expect('root@',timeout=20)
        #result.sendline('ls /')
        #result.expect(['bin','mnt','sys'],timeout=20)
        #print(result.readline().decode('ascii'))
        #result.sendline('exit')
        
        print('seccuss')
        result.interact()
    except pexpect.EOF:
        print('EOF')
        result.close()
    except pexpect.TIMEOUT:
        print('timeout')
        result.close()
        
        
if __name__ =='__main__':
    conssh(cmd1)


