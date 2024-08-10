from academic.model.Identifier import Identifier
from academic.model.Lecturer import Lecturer

class Course(Identifier):
    def __init__(self, code="", name="", credits=0, passGrade=""):
        super().__init__(code, name)
        self.__credits = credits
        self.__passGrade = passGrade
        self.__lecturer = ""

    def InfoLecturer(self, initial, listLecturer:Lecturer):
        sb = []
        count = 0
        lecInitial = initial.split(",")
        for lec in listLecturer:
            for i in lecInitial:
                if lec.getInitial() == i:
                    sb.append(f"{i} ({lec.getEmail()})")
                    if( count < len(lecInitial) - 1):
                        sb.append(";")
                        count += 1
        
        self.__lecturer = "".join(sb)
        
    def getLecturer(self):
        return self.__lecturer
    
    def getCredits(self)->int:
        return self.__credits
        
    def __str__(self):
        return super().__str__() + "|" + str(self.__credits) + "|" + str(self.__passGrade) + "|" + self.__lecturer
