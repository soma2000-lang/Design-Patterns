

import sys

#
# Component
# defines an interface for objects that can have responsibilities
# added to them dynamically
#
class Component:
  def operation(self):
    pass
  
#
# Concrete Component
# defines an object to which additional responsibilities
# can be attached
#
class ConcreteComponent(Component):
  def __init__(self):
    Component.__init__(self)

  def operation(self):
    print("Concrete Component operation")


class Decorator(Component):
  def __init__(self, component):
    Component.__init__(self)
    self._component = component

  def operation(self):
    self._component.operation()

class ConcreteDecoratorA(Decorator):
  def __init__(self, component):
    super().__init__(component)
  
  def operation(self):
    super().operation()
    print("Decorator A")

class ConcreteDecoratorB(Decorator):
  def __init__(self, component):
    super().__init__(component)
  
  def operation(self):
    super().operation()
    print("Decorator B")


if __name__ == "__main__":
  component = ConcreteDecoratorA(
        ConcreteDecoratorB( ConcreteComponent() ) )
              
  component.operation()