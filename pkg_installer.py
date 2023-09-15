from os import system as s
from os import mkdir
from os import chdir as cd
from sys import argv as a


def just_install(pkg):
  s(f'python -m pip install {pkg}')


def pkg_install(pkg):
  just_install('--upgrade pip')
  s(pkg)
  just_install('--upgrade pip')
  s(f'python -m pip uninstall {pkg}')
  just_install('--upgrade pip')
  s(pkg)
  just_install('--upgrade pip')
  s(f'--upgrade {pkg}')


def offline_install(pkg):
  just_install(f'--no-index -f . {pkg}')


def pkgs(func=pkg_install):
  func('numpy')
  func('tesseract')
  func('pillow')
  func('opencv-python')


def download_pkg(pkg):
  s(f'python -m pip download {pkg}')


def main():
  print(a)
  if len(a) > 1:
    cmds = a[1]
    if cmds == 'downloads':
      mkdir('pkgs')
      cd('pkgs')
      pkgs(func=download_pkg)
    elif cmds == 'offline':
      cd('pkgs')
      pkgs(func=offline_install)
    else:
      print(f'wrong parameter {cmds}, it must be downloads or offline or not')
  else:
    pkgs()


if __name__ == "__main__": main()
