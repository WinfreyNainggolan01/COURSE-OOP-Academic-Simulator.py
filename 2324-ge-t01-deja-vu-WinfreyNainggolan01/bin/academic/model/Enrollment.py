from academic.model.Course import Course
from academic.model.Student import Student


class Enrollment:
    def __init__(self, student, course, year, term, grade):
        self.__student = student
        self.__course = course
        self.__year = year
        self.__term = term
        self.__grade = grade
        
    def __init__(self):
        self.__student = Student()
        self.__course = Course()
        self.__year = 0
        self.__term = ""
        self.__grade = "None"

    def setStudent(self, student):
        self.__student = student
        
    def setCourse(self, course):
        self.__course = course
    
    def setGrade(self, grade):
        if grade == None:
            self.__grade = "None"
        else:
            self.__grade = grade

    def setYear(self, year):
        self.__year = year

    def setTerm(self, term):
        self.__term = term

    def getGrade(self) -> str:
        return self.__grade

    def __str__(self) -> str:
        return self.__student.getId() + "|" + self.__course.getCode() + "|" + str(self.__year) + "|" + self.__term + "|" + str(self.__grade)
    
