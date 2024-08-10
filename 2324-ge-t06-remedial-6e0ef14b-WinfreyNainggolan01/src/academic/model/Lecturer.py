from academic.model.Identifier import Identifier

class Lecturer(Identifier):
    
    def __init__(self, id="", name="", initial="", email="", studyProgram=""):
        super().__init__(id, name)
        self.__initial = initial
        self.__email = email
        self.__studyProgram = studyProgram
    
    def getEmail(self)->str:
        return self.__email
    
    def getInitial(self)->str:
        return self.__initial
    
    def __str__(self) -> str:
        return super().__str__() + "|" + self.__initial + "|" + self.__email + "|" + self.__studyProgram
    