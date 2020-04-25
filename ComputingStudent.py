# Multilevel inheritance in python
# https://www.programiz.com/python-programming/methods/built-in/super

class Student:
    def __init__(self):
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.gender = input("Gender: ")

    def printStudent(self):
        print("====print student details===")
        print(self.name)
        print(self.age)
        print(self.gender)

class ComputingStudent(Student):
    def __init__(self):
        #super(ComputingStudent, self).__init__()
        super().__init__()
        print("\nEnter the marks for your first three tests:")
        self.test1 = int(input("Test1:"))
        self.test2 = int(input("Test2:"))
        self.test3 = int(input("Test3:"))

    def getMarks(self):
        print("\ntest scores are:")
        print(self.test1)
        print(self.test2)
        print(self.test3)

class TopComputingStudnet(ComputingStudent):
    def __init__(self):
        #super(TopComputingStudnet, self).__init__()
        super().__init__()   # multilevel inheritance not need to specify the parent
        self.total_marks = self.test1 + self.test2 + self.test3

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Total Marks:", self.test1 + self.test2 + self.test3)

    def eligible_for_reward(self):
        if self.age > 18 and self.total_marks > 90:
            print("You are eligible for reward!")
        else:
            print("Sorry, you are not eligible for reward!")

if __name__ == "__main__":
    topcomputingstudent1 = TopComputingStudnet()
    topcomputingstudent1.getMarks()
    topcomputingstudent1.display()
    topcomputingstudent1.eligible_for_reward()
