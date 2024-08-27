#  a class only has one instance, and provide a global point of access to it. Pattern has creational purpose and deals with object relationships, which are more dynamic. The Singleton is often used as a part another design patterns


import sys



class Singleton:
  def __init__(self, instance):
    self._instance = instance

  def get(self):
    try:
      return self._only
    except AttributeError:
      self._only = self._instance()
      return self._only

  def __call__(self):
    raise TypeError("...")

@Singleton
class Class:
  def tell(self):
    print("This is singleton.")
 

if __name__ == "__main__": 
  singleton = Class.get()
  singleton.tell()                                                                                       