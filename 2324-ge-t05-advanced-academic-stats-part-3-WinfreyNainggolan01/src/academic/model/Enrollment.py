from academic.model.Course import Course
from academic.model.Student import Student

class Enrollment:
    def __init__(self, student=None, course=None, year=0, term="", grade=None):
        if student is None:
            self.__student = Student()
        else:
            self.__student = student

        if course is None:
            self.__course = Course()
        else:
            self.__course = course

        self.__year = year
        self.__term = term

        if grade is None:
            self.__grade = "None"
        else:
            self.__grade = grade

    def setStudent(self, student):
        self.__student = student
        
    def setCourse(self, course):
        self.__course = course
    
    def setGrade(self, grade:str):
        self.__grade = grade if grade is not None else "None"

    def setYear(self, year):
        self.__year = year

    def setTerm(self, term):
        self.__term = term

    def getGrade(self) -> str:
        return self.__grade
    
    def getYear(self) -> str:
        return self.__year
    
    def getTerm(self) -> str:
        return self.__term
    
    def getStudent(self) -> Student:
        return self.__student
    
    def getCourse(self) -> Course:
        return self.__course
    
    def gradeValue(_grade)->float:
        if _grade == "A":
            return 4.0
        elif _grade == "AB":
            return 3.5
        elif _grade == "B":
            return 3.0
        elif _grade == "BC":
            return 2.5
        elif _grade == "C":
            return 2.0
        elif _grade == "D":
            return 1.0
        elif _grade == "E":
            return 0.5
        else:
            return 0.0
        
    def __str__(self) -> str:
        return self.__course.getId() + "|" + self.__student.getId()   + "|" + str(self.__year) + "|" + self.__term + "|" + str(self.__grade)
