import os


def javac(path):
	filelist=os.listdir(path)
	javafile=[f for f in filelist if f.endswith('.java')]
	for f in javafile:
		doc=os.system('javac %s'%(os.path.join(path,f)))


def jfile(path):
	filelist=os.listdir(path)
	javafile=[f for f in filelist if f.endswith(('.java','.class'))]
	print(javafile)

if __name__ == '__main__':
	jfile('/home/chao/java')
