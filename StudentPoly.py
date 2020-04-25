# polymorphism in python
# It is the characteristic of an entity to be able to present in more than one form, having multiple behaviors.
# overriding: allow alternative implementation within the subclass to a method already defined in the super class
# overloading: allow different implementations with the same name within the same class, not very possible in python


class Student:
    def setNoOfCourses(self):
        self.numberofcourses = 3

    def displayNoOfCourses(self):
        print(self.numberofcourses)

class AdvancedStudent(Student):
    def setNoOfCourses(self):
        self.numberofcourses = 5 # redefining the base class method

    def resetNoOfCourses(self):
        super().setNoOfCourses() # point back to the base class

if __name__ == "__main__":
    student = Student()
    student.setNoOfCourses()
    print("Number of courses taken by the student: ")
    student.displayNoOfCourses()
    advanced_student = AdvancedStudent()
    advanced_student.setNoOfCourses()
    print("Number of courses taken by the advanced student: ")
    advanced_student.displayNoOfCourses()
    print("Number of courses taken by the advanced student after reset: ")
    advanced_student.resetNoOfCourses()
    advanced_student.displayNoOfCourses()