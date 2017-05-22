#/usr/bin/python3

import os

class Person(object):
	"""docstring for Person"""
	def __init__(self, arg=10):
		self.arg = arg

	def add(self,a):
		return self.arg+a


h=hasattr(Person(),'arg')
print(h)
print(Person().arg)

s='hello,world \n'
print(s)

l=[1,2,3]
';'.join(l)
d={'a':3,'b':4}



"""  
python learn note
"""
"""
(path,fileName)=os.path.split('/home/test.txt')

os.path.splitext()
os.listdir('/')
os.path.isdir()
"""
import os
import sys

def javac(path):
	filelist=os.listdir(path)
	javafile=[f for f in filelist if f.endswith('.java')]
	for f in javafile:
		doc=os.system('javac %s'%(os.path.join(path,f)))








if __name__ == '__main__':
	javac('/home/chao/java')
