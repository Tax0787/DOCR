from os import system as s
from os import mkdir
from os import chdir as cd
from sys import argv as a


def just_install(pkg, ver=''):
  s(f'python -m pip{ver} install {pkg}')


def updatepip(ver=''):
  just_install(f'--upgrade pip{ver}', ver=ver)


def pkg_install(pkg, ver=''):
  updatepip(ver=ver)
  just_install(pkg, ver=ver)
  updatepip(ver=ver)
  s(f'python -m pip{ver} uninstall {pkg}')
  updatepip(ver=ver)
  just_install(pkg, ver=ver)
  updatepip(ver=ver)
  just_install(f'--upgrade {pkg}', ver=ver)


def offline_install(pkg, ver=''):
  just_install(f'--no-index -f . {pkg}', ver=ver)


def pkgs(func=pkg_install, ver=''):
  func('numpy', ver=ver)
  func('tesseract', ver=ver)
  func('pillow', ver=ver)
  func('opencv-python', ver=ver)


def download_pkg(pkg, ver=''):
  s(f'python -m pip download {pkg}')


def main_with_ver(ver):
  if len(a) > 1:
    cmds = a[1]
    if cmds == 'downloads':
      mkdir('pkgs')
      cd('pkgs')
      pkgs(func=download_pkg, ver=ver)
    elif cmds == 'offline':
      cd('pkgs')
      pkgs(func=offline_install, ver=ver)
    else:
      print(f'wrong parameter {cmds}, it must be downloads or offline or not')
  else:
    pkgs(ver=ver)


def main():
  main_with_ver('3')


if __name__ == "__main__": main()
