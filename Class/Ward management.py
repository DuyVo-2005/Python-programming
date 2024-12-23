class Person:
    def __init__(self):
        self.name = ""
        self.yob = 0

    @property
    def yob(self):
        return self._yob

    @yob.setter
    def yob(self, value):
        while value < 0:
            print("Nam sinh khong hop le! Nhap lai nam sinh: ")
            value = int(input())
        self._yob = value

    def Input(self):
        self.name = input("Nhap ten: ")
        self.yob = int(input("Nhap nam sinh: "))

    def Describe(self):
        print(f"Ten: {self.name}")
        print(f"Nam sinh: {self.yob}")


class Student(Person):
    def __init__(self):
        super().__init__()
        self.grade = ""

    def Input(self):
        super().Input()
        self.grade = input("Nhap khoi: ")

    def Describe(self):
        super().Describe()
        print(f"Lop: {self.grade}")


class Ward:
    def __init__(self):
        self.name = ""
        self.personLst = []
    def AddPerson(Person):        
        pass    

class Doctor(Person):
    def __init__(self):
        super().__init__()
        self.specialist = ""

    def Input(self):
        super().Input()
        self.specialist = input("Nhap chuyen khoa: ")

    def Describe(self):
        super().Describe()
        print(f"Chuyen khoa: {self.specialist}")


class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.subject = ""

    def Input(self):
        super().Input()
        self.subject = input("Nhap mon giang day: ")

    def Describe(self):
        super().Describe()
        print(f"Mon giang day: {self.subject}")

a = Student()
b = Teacher()
c = Doctor()
a.Input()
b.Input()
c.Input()
a.Describe()
b.Describe()
c.Describe()
