from my_os_option import my_os, is_termux, installer
from os import system as s
from subprocess import run as start
from os import chdir as cd
from os import listdir as ls

posix_is_linux = None if my_os == 'Windows' else NotImplemented
posix_is_linux = True if my_os == 'Linux' else NotImplemented
posix_is_linux = False if my_os == 'Darwin' else NotImplemented

if posix_is_linux and is_termux:
  s('pkg install tesseract')
  s('pkg install which')
  print('\033[32mtesseract executable file path : ')
  s('which tesseract')
  print('\033[0m')
elif posix_is_linux:
  s('sudo apt install tesseract-ocr')
  print('\033[32mtesseract executable file path : ')
  s('which tesseract')
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
  print(f'{path}/tesseract.exe')
  print('\033[0m')
elif posix_is_linux == NotImplemented:
  raise posix_is_linux
else:
  s('brew install tesseract')
  print('\033[32mtesseract executable file path : ')
  s('cd / && sudo find . -iname tesseract')
  print('\033[0m')
