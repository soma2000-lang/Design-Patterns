# Template method defines the skeleton of an algorithm in an operation, deferring some
# steps to subclasses. It lets subclasses redefine certain steps of an algorithm 
# without changing the algorithm's structure. The pattern has behavioral purpose and
# applies to the classes.
# * to implement the invariant parts of an algorithm once and leave it up to subclasses to implement the behavior that can vary
# * when common behavior among subclasses should be factored and localizedin a common class to avoid code duplication
# * to control subclasses extensions
#
# Python Design Patterns: Template Method
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# AbstractClass
# implements a template method defining the skeleton of an algorithm
#
class AbstractClass:
  def templateMethod(self):
    self.primitiveOperation1()
    self.primitiveOperation2()

  def primitiveOperation1(self):
    pass
    
  def primitiveOperation2(self):
    pass

#
# Concrete Class
# implements the primitive operations to carry out specific steps
# of the algorithm, there may be many Concrete classes, each implementing
# the full set of the required operation
#
class ConcreteClass(AbstractClass):
  def __init__(self):
    AbstractClass.__init__(self)

  def primitiveOperation1(self):
    print("Primitive operation 1")

  def primitiveOperation2(self):
    print("Primitive operation 2")


if __name__ == "__main__":
  tm = ConcreteClass()
  tm.templateMethod()