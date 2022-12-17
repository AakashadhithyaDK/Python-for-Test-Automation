class StudentDetails:

    def __init__(self):
        self.rollno = 0
        self.name = ''
        self.m1 = self.m2 = self.m3 = 0

    def readData(self):
        self.rollno = int(input('Enter roll no'))
        self.name = input('Enter the name')
        self.m1 = int(input('Enter the mark1'))
        self.m2 = int(input('Enter the mark2'))
        self.m3 = int(input('Enter the mark3'))


class StudentGrade(StudentDetails):
    def __init__(self):
        StudentDetails.__init__(self)


    def calc(self):
        tot = self.m1 + self.m2 + self.m3
        avg = tot / 3
        return (tot, avg)


    def display(self, tot, avg):
        print(self.rollno, self.name, tot, avg)


sg = StudentGrade()
sg.readData()
tot, avg = sg.calc()
sg.display(tot, avg)
