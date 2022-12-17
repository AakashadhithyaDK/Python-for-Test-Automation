class studentmarks:
    def __init__(self):
        self.rollno=0
        self.name=''
        self.m1=self.m2=self.m3=0


    def readdata(self):
        self.rollno=int(input('Enter roll no'))
        self.name=input('Enter the name')
        self.m1=int(input('Enter the mark1'))
        self.m2 = int(input('Enter the mark2'))
        self.m3 = int(input('Enter the mark3'))


    def calc(self):
        tot=self.m1+self.m2+self.m3
        avg=tot/3
        return(tot,avg)

    def display(self,tot,avg):
        print(self.rollno,self.name,tot,avg)


sm1 = studentmarks()
sm1.readdata()
tot,avg = sm1.calc()
sm1.display(tot,avg)