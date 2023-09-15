from os import system as s2
from os import mkdir
from os import chdir as cd
from sys import argv as a


def s(x, prints=False):
  if prints:
    print(f'\t#{x}')
  s(x)


def just_install(pkg, ver='', prints=False):
  s(f'python -m pip{ver} install {pkg}', prints=prints)


def updatepip(ver='', prints=False):
  just_install(f'--upgrade pip{ver}', ver=ver, prints=prints)


def pkg_install(pkg, ver='', prints=False):
  updatepip(ver=ver, prints=prints)
  just_install(pkg, ver=ver, prints=prints)
  updatepip(ver=ver, prints=prints)
  s(f'python -m pip{ver} uninstall {pkg}', prints=prints)
  updatepip(ver=ver, prints=prints)
  just_install(pkg, ver=ver, prints=prints)
  updatepip(ver=ver, prints=prints)
  just_install(f'--upgrade {pkg}', ver=ver, prints=prints)


def offline_install(pkg, ver='', prints=False):
  just_install(f'--no-index -f . {pkg}', ver=ver, prints=prints)


def pkgs(func=pkg_install, ver='', prints=False):
  func('numpy', ver=ver, prints=prints)
  func('tesseract', ver=ver, prints=prints)
  func('pillow', ver=ver, prints=prints)
  func('opencv-python', ver=ver, prints=prints)


def download_pkg(pkg, ver='', prints=False):
  s(f'python -m pip download {pkg}', prints=prints)


def main_with_option(ver, debug):
  if len(a) > 1:
    cmds = a[1]
    if cmds == 'downloads':
      mkdir('pkgs')
      cd('pkgs')
      pkgs(func=download_pkg, ver=ver, prints=debug)
    elif cmds == 'offline':
      cd('pkgs')
      pkgs(func=offline_install, ver=ver, prints=debug)
    else:
      print(f'wrong parameter {cmds}, it must be downloads or offline or not')
  else:
    pkgs(ver=ver, prints=debug)


def main():
  main_with_option('3', True)


if __name__ == "__main__": main()
