import importer
from option import tesseract_path as tesseract_path_option

tesseract_path = tesseract_path_option


class LikeModule:
  __getattr__ = lambda self, x: self.__dict__[x]

  def __setattr__(self, x, y):
    self.__dict__[x] = y


class ImgLoad:
  lib = None

  def __init__(self, f):
    self.lib = self.Lib()
    self.__value = self.lib.open(f)

  def __call__(self):
    return self.lib.metrix(self.value)

  @property
  def value(self):
    return self.__value


class ImgLoader(ImgLoad):

  def Lib(self):
    ret = LikeModule()
    ret.open = importer.img.open
    ret.metrix = importer.metrix
    return ret
