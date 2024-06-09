from academic.model.Course import Course 

def main():
    while True:
        command = input()
        if command == "---":
            break
        else:
            data = command.split("#")
            course = Course(data[0], data[1], int(data[2]), data[3])
            print(course)

if __name__ == "__main__":
    main()
