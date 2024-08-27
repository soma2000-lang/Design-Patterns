# decouple an abstarction from its implementation so that they can vary independantly
#use it when you want to avoid a permanent binding between an abstarction and its impelmentation

import  sys
    class Implementator:
        def action(self):
            pass
    class ConcreteImplementorA(Implementator):
        def action(self):
            print("Concrete Implematator A")
    class ConcreteImplementatorB(Implementator):
        def action(self):
            print("Concrete Implemnattor B")
    class Bridge:
        def__init_(self,implementation):
            self._implementator=implementation
        def operation(self):
            self._implementator.action()
    if __name__=="__main__":
        bridge= Bridge(ConcreteImplementorA())
        bridge.operation()
        
        
        bridge=Bridge(ConcreteImplementatorB)
        bridge.operation()
            