# multiple inheritance in python
class Person:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

class Student:
    def __init__(self, studentId, subject):
        self.studentId = studentId
        self.subject = subject

    def getId(self):
        return self.studentId

class EnrolledStudent(Person, Student):
    def __init__(self, name, age, studentId, subject, enrolled_date):
        Person.__init__(self, name, age)   # multiple inheritance need to specify the parent
        Student.__init__(self, studentId, subject)
        self.enrolled_date = enrolled_date

    def getDate(self):
        return self.enrolled_date

if __name__ == "__main__":
    enrollstudent1 = EnrolledStudent("Joe Blue", 33, "001", "Computing 101", "19/01/10")
    enrollstudent1.showName()
    print("StudentId is", enrollstudent1.getId())