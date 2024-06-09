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
                
                if(not hasCourse(listCourse, data[1])):
                    print("invalid course|"+data[1])
                elif(not hasStudent(listStudent, data[2])):
                    print("invalid student|"+data[2])
                else:
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
    
    listCourse = sorted(listCourse, key=lambda course: course.getCode())
    for course in listCourse:
        print(course)
        
    listStudent = sorted(listStudent, key=lambda student: student.getId())
    for student in listStudent:
        print(student)
        
    for enrollment in listEnrollment:
        print(enrollment)
        
def hasCourse(listCourse, code)->bool:
    for course in listCourse:
        if course.getCode() == code:
            return True
    return False

def hasStudent(listStudent, id)->bool:
    for student in listStudent:
        if student.getId() == id:
            return True
    return False

if __name__ == "__main__":
    main()
