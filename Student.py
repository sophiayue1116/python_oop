class Student:
    def __init__(self, name, test_score):
        self.name = name
        self.test_score = test_score

    def hasAchievedTarget(self):
        if self.test_score >= 90:
            print("Target met, well done!")
        else:
            print("Target not achieved.")

#===create instance===
student1 = Student("Julia", 99)
print(student1.name)
print(student1.test_score)
student1.hasAchievedTarget()

