#  many related classes differ only in their behavior

# * you need different variants of an algorithm
# * an algorithm uses data that clients shouldn't know about
# import sys

#
# Strategy
# declares an interface common to all supported algorithms
#
class Strategy:
  def algorithmInterface(self):
    pass

#
# Concrete Strategies
# implement the algorithm using the Strategy interface
#
class ConcreteStrategyA(Strategy):
  def __init__(self):
    Strategy.__init__(self)
  
  def algorithmInterface(self):
    print("Concrete Strategy A")

class ConcreteStrategyB(Strategy):
  def __init__(self):
    Strategy.__init__(self)
  
  def algorithmInterface(self):
    print("Concrete Strategy B")

class ConcreteStrategyC(Strategy):
  def __init__(self):
    Strategy.__init__(self)
  
  def algorithmInterface(self):
    print("Concrete Strategy C")

#
# Context
# maintains a reference to a Strategy object
#
class Context:
  def __init__(self, strategy):
    self._strategy = strategy

  def contextInterface(self):
    self._strategy.algorithmInterface()


if __name__ == "__main__":
  strategy = ConcreteStrategyA()
    
  context = Context(strategy)
  context.contextInterface()