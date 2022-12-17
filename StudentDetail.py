class StudentDetails:

    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name

class StudentMarks():
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def show(self):
        print('hiee')


    '''def readData(self):
        self.rollno = int(input('Enter roll no'))
        self.name = input('Enter the name')
        self.m1 = int(input('Enter the mark1'))
        self.m2 = int(input('Enter the mark2'))
        self.m3 = int(input('Enter the mark3'))'''


class StudentGrade(StudentDetails,StudentMarks):
    def __init__(self,rollno,name,m1,m2,m3,tot,avg):
        #StudentDetails.__init__(self,rollno,name,m1,m2,m3)
        super(StudentGrade,self).__init__(rollno,name)
        StudentMarks.__init__(self,m1,m2,m3)
        self.tot=tot
        self.avg=avg

    def show(self):
        print('welcome')


    def calc(self):
        self.tot = self.m1 + self.m2 + self.m3
        self.avg = self.tot / 3


    def display(self):
        print(self.rollno, self.name, self.tot, self.avg)


sg = StudentGrade(12,'aed',100,100,100,0,0)
#sg.readData()
sg.show()
sg.calc()
sg.display()

