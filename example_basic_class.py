class Ward:
    def __init__(self):
        self.name = ""
        self.perLst = []
    def AddPerson(self, person):    
        self.perLst.append(person)
        
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
            value = int(input("Nhap nam sinh hop le: "))
        self._yob = value
    def Input(self):
        self.name = input("Nhap ten: ")
        self.yob = int(input("Nhap tuoi: "))
    def Describe(self):
        print(f"Ten: {self.name}")
        print(f"Tuoi: {self.yob}")
        
        
class Student(Person):
    def __init__(self):
        super().__init__()
        self.grade = ""
    def Input(self):
        super().Input()
        self.grade = input("Nhap lop: ")
    def Describe(self):
        super().Describe()
        print(f"Lop: {self.grade}")


class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.subject = ""
    def Input(self):
        super().Input()
        self.subject = input("Nhap mon: ")
    def Describe(self):
        super().Describe()
        print(f"Mon: {self.subject}")
        
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

def aveTeacherYearOfBirth(PerLst):
     lst = []
     sumAge = 0
     for person in PerLst:
         if isinstance(person, Teacher):
            lst.append(person)
     for i in lst:
         sumAge += i.yob
     return sumAge/len(lst)
                        
ward = Ward() 
choice = - 1          
while choice != 0:
    print("1. Hoc sinh")   
    print("2. Giao vien")
    print("3. Bac si")
    print("0. Dung viec nhap")
    choice = int(input("Nhap lua chon: "))
    if choice == 0:
        break
    elif choice == 1:
        tmp = Student()
        tmp.Input() 
        ward.AddPerson(tmp)   
    elif choice == 2:#
        tmp = Teacher()
        tmp.Input()  
        ward.AddPerson(tmp)
    elif choice == 3:
         tmp = Doctor()
         tmp.Input()
         ward.AddPerson(tmp)
countDoctor = 0
for person in ward.perLst:
    if isinstance(person,Doctor):
        countDoctor += 1
print(f"Số lượng bác sĩ:  {countDoctor}")

ward.perLst.sort(key = lambda person: person.yob)

print("Danh sách người sau khi xếp tăng dần tuổi: ")
[person.Describe() for person in ward.perLst]

print(f"Tuổi trung bình của giáo viên trong phường: {aveTeacherYearOfBirth(ward.perLst)}")
#Cải tiến: các thuộc tính nên private:
#__name_property
#cài get_name_property,
#set_name_property
#vd: xem oop cuối kỳ
