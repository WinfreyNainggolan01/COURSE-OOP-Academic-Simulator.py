

class Course:
    def __init__(self, code, name, credits, passGrade):
        self.__code = code
        self.__name = name
        self.__credits = credits
        self.__passGrade = passGrade
        
    def __init__(self):
        self.__code = ""
        self.__name = ""
        self.__credits = 0
        self.__passGrade = ""

    def setCode(self, code):
        self.__code = code

    def getCode(self):
        return self.__code
    
    def __str__(self):
        return self.__code + "|" + self.__name + "|" + str(self.__credits) + "|" + str(self.__passGrade)


    
