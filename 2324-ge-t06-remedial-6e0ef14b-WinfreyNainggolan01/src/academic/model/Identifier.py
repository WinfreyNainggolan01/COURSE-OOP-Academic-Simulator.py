class Identifier():
    def __init__(self, id="", name=""):
        self.__id = id
        self.__name = name
        
    def getId(self)->str:
        return self.__id
    
    def getName(self)->str:
        return self.__name
    
    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name
    
    def __str__(self) -> str:
        return self.__id + "|" + self.__name