import sys
from academic.model.Student import Student


def main():
    student = Student(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    
    print(student)
    
if __name__ == "__main__":
    main()