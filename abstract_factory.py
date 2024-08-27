import sys 
# used so thta functions are strongly bound with the interpreter
class ProductA:
        def getName(self):
            pass
class ConcreteFactoryAX(ProductA):
    def getName(self):
         return "AX"
class ConcreteFactoryAY(ProductA):
    def getName(self):
         return "AY"
class ProductB:
            def getName(self):
                pass
class ConcreteFactoryAX(ProductA):
    def getName(self):
         return "AX"
class ConcreteFactoryBY(ProductB):
    def getName(self):
         return "BY"
class AbstractFactory:
    def createProductA(self):
        pass
    def createProductB(self):
        pass
class ConcreteFactoryX(AbstractFactory):
    def createProductA(self):
         return ConcreteFactoryAX()
    def createProductB(self):
         return ConcreteFactoryBY() 
if __name__=="__main__":
    factoryX =ConcreteFactoryX()
    factoryY =ConcreteFactoryY()
    
    p1=factoryX.createProductA()
    print("Product:" +p1.getName())
    p2=factoryY.createProductB()
    print("Product B"+p2.getName())