#!/usr/bin/python3

import urllib.request
import re
import os

host='https://apps.fedoraproject.org'
url='https://apps.fedoraproject.org/nuancier/results/6/'
lpath='/home/chao/Pictures/wallpaper'



def downhtml(url):
	stream=urllib.request.urlopen(url)
	html=stream.read()

	return html

def getimgurl(html):
	pt=re.compile(r'<a\s*href="(.*?)".*?>.*?<img',re.DOTALL)
	result=re.findall(pt,str(html))
	return result

def write2file(urls):
	i=0

	for ul in urls:
		fn=os.path.split(ul)[1]

		name=os.path.join(lpath,fn)
		u=host+ul
		try:
			urllib.request.urlretrieve(u,name)
		except Exception as e:
			print('download error:',e)
		 
		print(str(i)+'    '+fn)
		i+=1
		

sname='test.py'

def myname(path):
	isex=os.path.exists(path)
	if isex==False:
		return path
	else:
		pre,ext=os.path.splitext(path)
		name=(pre+'(%s)'+ext)
		return getname(name,1)





def getname(name,num):
    newname=name%(num)
    isex=os.path.exists(newname)
    if isex==False:
    	return newname
    else:
    	num=num+1
    	return getname(name,num)

		

	



if __name__ == '__main__':
	ss=os.path.join('/home/chao/python/',sname)
	print(myname(ss))

	# ht=downhtml(url)
	# #ht=os.read('home/chao/Desktop/source.html')
	# r=getimgurl(ht)
	
	# write2file(r)
	# print('complete')

