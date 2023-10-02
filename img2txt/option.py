from os.path import isfile as i
from os import chdir as cd
from os import getcwd as pwd
from os.path import dirname

class NoTesseractOCRError:
  pass

root = pwd()
cd(dirname(__file__))

if i('.tesseract_path.txt'):
  with open('.tesseract_path.txt') as f:
    tesseract_path = f.read()
elif i('.not_dev'):
  with open('.not_dev') as f:
    mod = f.read()
  if mod == 'option':
    print('\033[31mError : No Tesseract OCR\033[0m')
    exit(1)
  else:
    mod = __import__(mod)
    mod.core()
else:
  raise NoTesseractOCRError("tesseractOCR wasn't installed")

cd(root)