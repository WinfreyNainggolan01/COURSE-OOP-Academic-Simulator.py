from academic.model.Identifier import Identifier

class Student(Identifier):
    def __init__(self, id="", name="", year="", studyProgram=""):
        super().__init__(id, name)
        self.__year = year
        self.__studyProgram = studyProgram
        self.__gpa = 0.0
        self.__totalCredits = 0
    
    def setYear(self, year):
        self.__year = year
    
    def setStudyProgram(self, studyProgram):
        self.__studyProgram = studyProgram
        
    def setTotalCredits(self, totalCredits):
        self.__totalCredits = totalCredits
    
    def setGpa(self, gpa):
        self.__gpa = gpa
    
    def __str__(self) -> str:
        return super().__str__() + "|" + self.__year + "|" + self.__studyProgram
    
    def __repr__(self) -> str:
        return super().__str__() + "|" + self.__year + "|" + self.__studyProgram + "|" + "{:.2f}".format(self.__gpa) + "|" + str(self.__totalCredits) 