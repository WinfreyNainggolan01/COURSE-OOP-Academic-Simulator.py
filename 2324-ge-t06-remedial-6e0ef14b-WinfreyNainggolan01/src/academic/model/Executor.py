from academic.model.Course import Course
from academic.model.Enrollment import Enrollment
from academic.model.Lecturer import Lecturer
from academic.model.Student import Student
from academic.model.EnumGrade import EnumGrade

listCourse = []
listStudent = []
listEnrollment = []
listLecturer = []

class Executor:
    
    
    def __init__(self):
        pass
    
    def ctrlStudent(data):
        if(hasStudent(listStudent, data[1])):
            pass
        else:    
            student = Student(data[1], data[2], data[3], data[4])
            listStudent.append(student)
            
    def ctrlStudentDetails(data):
        totalCredits = 0
        value = 0
        tempCrsId = "" 
        tempGrade = ""
        for enr in listEnrollment:
            if enr.getStudent().getId() == data[1]:
                for course in listCourse:
                    if course.getId() == enr.getCourse().getId():
                        if enr.getCourse().getId() == tempCrsId:
                            value -= EnumGrade.get_scale(tempGrade) * course.getCredits()
                            totalCredits -= enr.getCourse().getCredits()
                        if enr.getRemedial() != None:
                            value += EnumGrade.get_scale(enr.getRemedial()) * course.getCredits()
                            totalCredits += enr.getCourse().getCredits()
                            tempGrade = enr.getRemedial()
                        else:
                            value += EnumGrade.get_scale(enr.getGrade()) * course.getCredits()
                            totalCredits += enr.getCourse().getCredits()
                            tempGrade = enr.getGrade()
                        
                        tempCrsId = enr.getCourse().getId()

        student = next((student for student in listStudent if student.getId() == data[1]), None)
        if student:
            if value != 0:
                student.setGpa(round(value / totalCredits, 2))
                student.setTotalCredits(totalCredits)
            else:
                student.setGpa(0.0)
                student.setTotalCredits(0)
            print(repr(student))
            
    def ctrlCourse(data):
        if(hasCourse(listCourse, data[1])):
            pass
        else:
            course = Course(data[1], data[2], int(data[3]), data[4])
            course.InfoLecturer(data[5], listLecturer)
            listCourse.append(course)
        
    def ctrlLecturer(data):
        if(hasLecturer(listLecturer, data[1])):
            pass
        else:
            lecturer = Lecturer(data[1], data[2], data[3], data[4], data[5])
            listLecturer.append(lecturer)
        
    def ctrlEnrollment(data):
        if(not hasCourse(listCourse, data[1])):
            pass
        elif(not hasStudent(listStudent, data[2])):
            pass
        else:
            course = next((course for course in listCourse if course.getId() == data[1]), None)
            student = next((student for student in listStudent if student.getId() == data[2]), None)
            
            if course and student:
                enrollment = Enrollment(student, course, data[3], data[4])
                listEnrollment.append(enrollment)
                
    def ctrlEnrollmentGrade(data):
        for enrollment in listEnrollment:
            if enrollment.getCourse().getId() == data[1] and enrollment.getStudent().getId() == data[2] and enrollment.getYear() == data[3] and enrollment.getTerm() == data[4]:
                enrollment.setGrade(data[5])
                break
            
    def ctrlEnrollmentRemedial(data):
        for enrollment in listEnrollment:
            if enrollment.getCourse().getId() == data[1] and enrollment.getStudent().getId() == data[2] and enrollment.getYear() == data[3]:
                if enrollment.getGrade() == "None":
                    break
                else:
                    for student in listStudent:
                        if student.getId() == data[2]:
                            if enrollment.getFlagRemedial() == False:
                                enrollment.setRemedial(data[5])
                                enrollment.setFlagRemedial(True)
                                break
        
    def printElement():
        global listCourse, listStudent, listEnrollment, listLecturer
        for lecturer in listLecturer:
            print(lecturer)
        listCourse = sorted(listCourse, key=lambda course: course.getId())
        for course in listCourse:
            print(course)
        for student in listStudent:
            print(student)
        for enrollment in listEnrollment:
            if enrollment.getRemedial() != None:
                print(repr(enrollment))
            else:
                print(enrollment)
    
        
        
def hasCourse(listCourse, code)->bool:
    for course in listCourse:
        if course.getId() == code:
            return True
    return False

def hasStudent(listStudent, id)->bool:
    for student in listStudent:
        if student.getId() == id:
            return True
    return False

def hasLecturer(listLecturer, id)->bool:
    for lecturer in listLecturer:
        if lecturer.getId() == id:
            return True
    return False


    