from academic.model.Course import Course
from academic.model.Student import Student
from academic.model.Enrollment import Enrollment


def main():
    student = Student()
    course = Course()
    enrollment = Enrollment()
    
    student.setId(input())
    course.setCode(input())
    
    enrollment.setStudent(student)
    enrollment.setCourse(course)
    
    enrollment.setYear(input())
    enrollment.setTerm(input())
    enrollment.setGrade(None)
    
    print(enrollment)
    
    
if __name__ == "__main__":
    main()
    
    