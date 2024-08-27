class Strategy:
  def algorithmInterface(self):
    pass


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


class Context:
  def __init__(self, strategy):
    self._strategy = strategy

  def contextInterface(self):
    self._strategy.algorithmInterface()


if __name__ == "__main__":
  strategy = ConcreteStrategyA()
    
  context = Context(strategy)
  context.contextInterface()