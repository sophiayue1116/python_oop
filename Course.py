# Inheritance in Python
class Course:
    name = "Python Course"
    contactWebsite = "www.learnpython.com"

    def contactDetails(self):
        print("To contact us, simply go to", self.contactWebsite)

class OOPCourse(Course):
    def __init__(self):
        self.description = "Course on OOP fundimentals"
        self.trainer = "Mrs Tang"

    def trainerDetails(self):
        print("This course is about", self.description, "and it's run by ", self.trainer, ".")


course1 = OOPCourse()
course1.contactDetails()
course1.trainerDetails()