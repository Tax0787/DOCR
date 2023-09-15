import importer


class ImgLoad:
  lib = None

  def __init__(self, f):
    self.__value == lib.open(f)

  def __call__(self):
    return lib.metrix(self)

  @property
  def value(self):
    return self.__value


class ImgLoader(ImgLoad):

  class lib:
    open = importer.img.open
    metrix = importer.metrix
