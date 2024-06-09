from academic.model.Course import Course 
from academic.model.Student import Student
from academic.model.Enrollment import Enrollment

def main():
    listCourse = []
    listStudent = []
    listEnrollment = []

    while True:
        command = input()
        if command == "---":
            break
        else:
            data = command.split("#")
            if data[0] == "course-add":
                course = Course(data[1], data[2], int(data[3]), data[4])
                listCourse.append(course)
            elif data[0] == "student-add":
                student = Student(data[1], data[2], data[3], data[4])
                listStudent.append(student)
            elif data[0] == "enrollment-add":
                enrollment = Enrollment()
                student = Student()
                course = Course()
                
                student.setId(data[1])
                course.setCode(data[2])
                
                enrollment.setStudent(student)
                enrollment.setCourse(course)
                enrollment.setYear(data[3])
                enrollment.setTerm(data[4])
                enrollment.setGrade(None)
                listEnrollment.append(enrollment)

    for course in listCourse:
        print(course)
    for student in listStudent:
        print(student)
    for enrollment in listEnrollment:
        print(enrollment)

if __name__ == "__main__":
    main()
