from os.path import *

print(abspath('python.exe'))
print(basename('c:\\work\\python.exe'))

fileName = r'c:\Python310\python.exe'

if exists(fileName):
    print('파일크기:{0}'.format(getsize(fileName)))

import os

#print(os.name)
#print(os.environ)
#os.system('notepad.exe')

import glob

print(glob.glob(r'c:\work\*.py'))
print(glob.glob('*.py'))