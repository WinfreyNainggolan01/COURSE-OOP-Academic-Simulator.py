from academic.model.Course import Course 
from academic.model.Student import Student
from academic.model.Enrollment import Enrollment

def main():
    
    while True:
        command = input()
        if command == "---" :
            break
        else:
            data = command.split("#")
            enrollemnt = Enrollment()
            student = Student()
            course = Course()
            
            student.setId(data[0])
            course.setCode(data[1])
            
            enrollemnt.setStudent(student)
            enrollemnt.setCourse(course)
            enrollemnt.setYear(data[2])
            enrollemnt.setTerm(data[3])
            enrollemnt.setGrade(None)
            
            print(enrollemnt)
            

if __name__ == "__main__":
    main()
            
            
            
            
    