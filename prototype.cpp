 #Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype. Pattern has creational purpose and deals with object relationships, which are more dynamic. The pattern hides the complexities of making new instances from the client.


import sys
import copy


class Prototype:
  def clone(self):
    pass
  
  def getType(self):
    pass

class ConcretePrototypeA(Prototype):
  def clone(self):
    return copy.deepcopy(self)
  
  def getType(self):
    return "type A"  

class ConcretePrototypeB(Prototype):
  def clone(self):
    return copy.deepcopy(self)
  
  def getType(self):
    return "type B"  

class Client:
  def __init__(self):
    self._types = [ConcretePrototypeA(), ConcretePrototypeB()]
  
  def make(self, index):
    return self._types[index].clone()     


if __name__ == "__main__":
  client = Client()
  
  prototype = client.make(0)
  print(prototype.getType())
  
  prototype = client.make(1)
  print(prototype.getType())