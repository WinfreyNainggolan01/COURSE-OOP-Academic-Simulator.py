from academic.model import *

class Student:
    def __init__(self, id="", name="", gpa=0.0, credits=0):
        self.__id = id
        self.__name = name
        self.__gpa = gpa
        self.__credits = credits
        
    def getId(self) -> str:
        return self.__id
    def getGpa(self) -> float:
        return self.__gpa
    
    def __str__(self) ->str:
        return f"{self.__id}|{self.__name}|{self.__gpa:.2f}|{self.__credits}"