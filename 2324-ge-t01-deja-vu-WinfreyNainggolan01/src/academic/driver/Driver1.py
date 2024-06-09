import sys
from academic.model.Course import Course


def main():
    course = Course(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])
    
    print(course)
    
if __name__ == "__main__":
    main()