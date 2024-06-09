class Course:
    def __init__(self, code="", name="", credits=0, passGrade=""):
        self.__code = code
        self.__name = name
        self.__credits = credits
        self.__passGrade = passGrade

    def setCode(self, code):
        self.__code = code

    def getCode(self):
        return self.__code
    
    def __str__(self):
        return self.__code + "|" + self.__name + "|" + str(self.__credits) + "|" + str(self.__passGrade)
