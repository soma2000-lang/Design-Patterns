
import sys

#The pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class. It has behavioral purpose and applies to the objects
#when an object's behavior depends on its state, and it must change its behavior at run-time depending on that state
#operations have large, multipart conditional statements that depend on the object's state


class State:
  def handle(self):
    pass

#
# Concrete States
# each subclass implements a behavior associated with a state
# of the Context
#
class ConcreteStateA(State):
  def __init__(self):
    State.__init__(self)
  
  def handle(self):
    print("State A handled.")

class ConcreteStateB(State):
  def __init__(self):
    State.__init__(self)  
  
  def handle(self):
    print("State B handled.")

#
# Context
# defines the interface of interest to clients
#
class Context:
  def __init__(self):
    self._state = State()
    
  def setState(self, state):
    self._state = state

  def request(self):
    self._state.handle()


if __name__ == "__main__":
  stateA = ConcreteStateA()
  stateB = ConcreteStateB()
  
  context = Context()
  
  context.setState(stateA)
  context.request()

  context.setState(stateB)
  context.request()