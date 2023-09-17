from os import system as s2
from os import mkdir
from os import chdir as cd
from sys import argv as a


def s(x, prints=False):
  if prints:
    print(f'\t#{x}')
  s2(x)


def just_install(pkg, ver='', prints=False, py = "python -m "):
  s(f'{py}-m pip{ver} install {pkg}', prints=prints)


def updatepip(ver='', prints=False,py = "python -m "):
  just_install(f'--upgrade pip{ver}', ver=ver, prints=prints, py=py)


def pkg_install(pkg, ver='', prints=False, py="python -m "):
  updatepip(ver=ver, prints=prints,py=py)
  just_install(pkg, ver=ver, prints=prints,py=py)
  updatepip(ver=ver, prints=prints,py=py)
  s(f'{py}pip{ver} uninstall {pkg}', prints=prints)
  updatepip(ver=ver, prints=prints,py=py)
  just_install(pkg, ver=ver, prints=prints,py=py)
  updatepip(ver=ver, prints=prints,py=py)
  just_install(f'--upgrade {pkg}', ver=ver, prints=prints,py=py)


def offline_install(pkg, ver='', prints=False, py = "python -m "):
  just_install(f'--no-index -f . {pkg}', ver=ver, prints=prints,py=py)


def pkgs(func=pkg_install, ver='', prints=False,py="python -m "):
  func('numpy', ver=ver, prints=prints,py=py)
  func('tesseract', ver=ver, prints=prints,py=py)
  func('pillow', ver=ver, prints=prints,py=py)
  func('opencv-python', ver=ver, prints=prints,py=py)


def download_pkg(pkg, ver='', prints=False,py="python -m "):
  s(f'{py}pip{ver} download {pkg}', prints=prints)


def main_with_option(ver, debugs, py):
  if len(a) > 1:
    cmds = a[1]
    if cmds == 'downloads':
      mkdir('pkgs')
      cd('pkgs')
      pkgs(func=download_pkg, ver=ver, prints=debugs, py=py)
    elif cmds == 'offline':
      cd('pkgs')
      pkgs(func=offline_install, ver=ver, prints=debugs,py=py)
    else:
      print(f'wrong parameter {cmds}, it must be downloads or offline or not')
  else:
    pkgs(ver=ver, prints=debugs,py=py)


def main():
  main_with_option('', False, '')


if __name__ == "__main__": main()
