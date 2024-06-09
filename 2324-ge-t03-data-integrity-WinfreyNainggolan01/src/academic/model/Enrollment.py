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
    
    def setGrade(self, grade):
        self.__grade = grade if grade is not None else "None"

    def setYear(self, year):
        self.__year = year

    def setTerm(self, term):
        self.__term = term

    def getGrade(self) -> str:
        return self.__grade

    def __str__(self) -> str:
        return self.__student.getId() + "|" + self.__course.getCode() + "|" + str(self.__year) + "|" + self.__term + "|" + str(self.__grade)
