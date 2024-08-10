from academic.model.Executor import Executor


def main():
    while True:
        command = input()
        if command == "---":
            break
        else:
            data = command.split("#")
            if data[0] == "course-add":
                Executor.ctrlCourse(data)
            elif data[0] == "student-add":
                Executor.ctrlStudent(data)
            elif data[0] == "enrollment-add":
                Executor.ctrlEnrollment(data)
            elif data[0] == "enrollment-grade":
                Executor.ctrlEnrollmentGrade(data)
            elif data[0] == "lecturer-add":
                Executor.ctrlLecturer(data)
            elif data[0] == "student-details":
                Executor.ctrlStudentDetails(data)
            elif data[0] == "enrollment-remedial":
                Executor.ctrlEnrollmentRemedial(data)
    Executor.printElement()

if __name__ == "__main__":
    main()
