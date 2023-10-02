def f(x):
  return x


from prelib import *


def imgf2str(files, img2txt=img2txt, ImgLoader=ImgLoader):
  return img2txt(f(ImgLoader(files)()))


def imgf2txtf(f1, f2, imgf2str=imgf2str, writer=o):
  return writer(f2, imgf2str(f1))
