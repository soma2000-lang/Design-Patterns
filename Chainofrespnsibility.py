#chain of reposnsibility  pattern its gives  more than an object a achance to
# handle the request
# you want to issue an object to several objects without  receiving the receiver explicitly
# the set of objects that can handle an requests should be specified dynamically


import sys 
class Handler:
    def __init__(self) -> None:
        successor=None
    def setHandler(self,successor):
        self._successor=successor
    def handleRequest(self):
        if (self._successor is not None):
            self._successor.handleRequest()
            
# concrete handlers the requests they are responsible for
class ConcreteHandler(Handler):
    def __int__(self):
        Handler.__init__(self)
        self._can_handle =False
    def handleRequest(self):
        if(self._can_handle):
            print("CAnnot be handled by handler !")
        else:
            print("Cannot be handled by handler 1")
            super().handleRequest()    
class Conceretehandler2(Handler):
    def __int__(self):
        Handler.__init__(self)
        self._can_handle =False
    def handleRequest(self):
        if(self._can_handle):
            print("CAnnot be handled by handler !")
        else:
            print("Cannot be handled by handler 1")
            super().handleRequest()   
    if __name__=="__main__":
        handler1 = ConcreteHandler1()
        handler2= ConcreteHandler2()
        handler1.handlerequest()
        handler2.handlerequest()
     
        