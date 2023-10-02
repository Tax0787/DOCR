from my_os_option import my_os, is_termux, installer, is_replit
from os import system as s
from subprocess import run as start
from os import chdir as cd
from os import listdir as ls
from os import popen as sNo

posix_is_linux = NotImplemented
posix_is_linux = None if my_os == 'Windows' else posix_is_linux
posix_is_linux = True if my_os == 'Linux' else posix_is_linux
posix_is_linux = False if my_os == 'Darwin' else posix_is_linux

f = open('.tesseract_path.txt', 'w')
if posix_is_linux and is_termux:
  s('pkg install tesseract')
  s('pkg install which')
  print('\033[32mtesseract executable file path : ')
  x = sNo('which tesseract').read()
  f.write(x)
  print(x)
  print('\033[0m')
elif posix_is_linux:
  sudo = '' if is_replit else 'sudo'
  s(f'{sudo} apt install tesseract-ocr')
  print('\033[32mtesseract executable file path : ')
  x = sNo('which tesseract').read()
  f.write(x)
  print(x)
  print('\033[0m')
elif posix_is_linux == None:
  cd('WindowsTesseractInstall')
  s(f'curl -lo {installer}')
  now = ls()
  now.remove('.')
  now.remove('..')
  start(now.pop())
  cd('..')
  path = input('install path : ')
  s(f'setx PATH "%PATH%;{path}" -m')
  print('\033[32mtesseract executable file path : ')
  print(f'{path}/tesseract.exe', file=f)
  print('\033[0m')
elif posix_is_linux == NotImplemented:
  f.close()
  raise posix_is_linux
else:
  s('brew install tesseract')
  print('\033[32mtesseract executable file path : ')
  x = sNo('cd / && sudo find . -iname tesseract').read()
  f.write(x)
  print(x)
  print('\033[0m')
f.close()
