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
            student = Student(data[0], data[1], data[2], data[3])
            print(student)

if __name__ == "__main__":
    main()