class Student:
    def GetStudentData(self):
        self.rollno=int(input('enter roll no ='))
        self.name=input('enter name =')

class Test (Student):
    def MarksTest(self):
        self.English = int(input('enter english Marks='))
        self.Maths = int(input('enter Maths Marks='))

class Sport(Student) :
    def SportsTest(self):
        self.sport=int(input('enter sports marks='))

class Result(Sport,Test):
    def ResultDisplay(self):
        print(f'Name Of Student Is {self.name} and roll number is {self.rollno}')
        avg=(self.English+self.Maths)
        print('Average of Test Subject is ',avg)
        print(f'Marks of Sports are{self.sport}')

p1=Result()
a=p1.GetStudentData()
b=p1.MarksTest()
c=p1.SportsTest()
d=p1.ResultDisplay()
        