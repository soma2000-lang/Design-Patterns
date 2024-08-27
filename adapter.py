# you want to create resuable class that cooperates  with classes thta dont necessariy have compatible interfaces
import sys
class Target:
    def request(self):
        pass
class Adaptee: # this is the one which will give request
     def  specificRequest(self):
         print("Specific requeust")
class Adapter(Target,Adaptee):
    def __init__(self) -> None:
        Adaptee__init__(self)
        Target__init__(self)
    def request(self):
        return self.specificRequest()
if __name__ == '__main__':
    t= Adapter()
    t.request()
    
    