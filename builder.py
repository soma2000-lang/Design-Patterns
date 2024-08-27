the algorithm  for creating an object should be independant of the parts
and how it should be assembled,often used  building constrcuting objects

import sys

class Product:
    def __init__(self):
        self._partA=""
        self._partB=""
        self._partC=""
        def  makeA(self,part):
            self._partA= part
        def makeB(self,part):
            self._partB=part
        def makeC(self,part):
            self._partC=part
        