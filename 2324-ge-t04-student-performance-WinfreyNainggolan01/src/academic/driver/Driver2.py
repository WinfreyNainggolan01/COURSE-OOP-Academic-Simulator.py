from academic.model.Student import Student

def main():
    listStudent = []
    while True:
        command = input()
        if command == "---":
            break
        else:
            data = command.split("#")
            if data[0] == "student-add":
                student = Student(data[1], data[2], float(data[3]), int(data[4]))
                listStudent = sorted(listStudent, key=lambda s: s.getId())
                listStudent.append(student)
            elif data[0] == "student-show-all":
                showAllStudent(listStudent)
            elif data[0] == "student-best":
                listStudent = sorted(listStudent, key=lambda s: s.getGpa(), reverse=True)
                
                for i in listStudent[:int(data[1])]:
                    print(i)
                
        
def showAllStudent(listStudent):
    for student in listStudent:
        print(student)

if __name__ == "__main__":
    main()
