from academic.model import *

class Student:
    def __init__(self, id="", name="", year="", studyProgram=""):
        self.__id = id
        self.__name = name
        self.__year = year
        self.__studyProgram = studyProgram
    
    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setYear(self, year):
        self.__year = year
    
    def setStudyProgram(self, studyProgram):
        self.__studyProgram = studyProgram

    def getId(self) -> str:
        return self.__id
    
    def __str__(self) ->str:
        return self.__id + "|" + self.__name + "|" + self.__year + "|" + self.__studyProgram