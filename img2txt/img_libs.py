import importer


class ImgLoad:
  lib = None

  def __init__(self, f):
    self.lib = self.Lib()
    self.__value = self.lib.open(f)

  def __call__(self):
    return self.lib.metrix(self)

  @property
  def value(self):
    return self.__value


class ImgLoader(ImgLoad):

  class Lib:
    open = importer.img.open
    metrix = importer.metrix
