#coding = utf8


class Proxy(object):
  def __init__(self, subject):
    self.__subject = subject
  def __getattr__(self, name):
    return getattr(self.__subject, name)

class RGB:
  def __init__(self, red, green, blue):
    self.__red = red
    self.__green = green
    self.__blue = blue
  def Red(self):
    return self.__red
  def Green(self):
    return self.__green
  def Blue(self):
    return self.__blue

class NoBlueProxy(Proxy):
  def Blue(self):
    return 0

if __name__ == '__main__':
  rgb = RGB(100, 192, 240)
  print rgb.Red()
  proxy = Proxy(rgb)
  print proxy.Green()
  noblue = NoBlueProxy(rgb)
  print noblue.Green()
  print noblue.Blue()
