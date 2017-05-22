#!/usr/bin/python3


import pexpect
import time

name='root'
ip='45.76.96.188'
port='22'
password='[Ba7--5FXgC$U)Wt'

cmd='ssh -f -N -D 7075 %s@%s'%(name,ip)

#if len(sys.argv)>1:
#    pass

def conssh(cmd):

    try:
        result=pexpect.spawn(cmd)
        print('ssh start')
        i=result.expect(['password:','continue connecting (yes/no)?'],timeout=60)
        print('password:%d'%(i))
        if i==1:
            result.sendline('yes')
            result.expect('password:',timeout=20)
        print(result.after.decode('utf-8')+'*'*6)	
        result.sendline(password)
        #result.expect('root@',timeout=20)
        #result.sendline('ls /')
        #result.expect(['bin','mnt','sys'],timeout=20)
        #print(result.readline().decode('ascii'))
        #result.sendline('exit')
        print('seccuss')
        result.wait()
    except pexpect.EOF:
        print('EOF')
        result.close()
    except pexpect.TIMEOUT:
        print('timeout')
        result.close()

if __name__ =='__main__':
    conssh(cmd)
    


