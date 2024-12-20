import math as mh

def laCP(n):
    if n < 0:
        return False
    can = int(mh.sqrt(n))
    if can**2 != n:
            return False
    return True

n = int(input("Nhap 1 so nguyen: "))
    
if laCP(n):
    print(f"{n} la so chinh phuong")
else:
    print(f"{n} khong phai so chinh phuong")
    cpGanNhat = -99999
    if n < 0:
        cpGanNhat = 0
    else:
        cpTren = cpDuoi = n
        while not laCP(cpTren) and not laCP(cpDuoi):
            cpTren += 1
            cpDuoi -= 1
            if laCP(cpTren):
                cpGanNhat = cpTren
                break
            elif laCP(cpDuoi):
                cpGanNhat = cpDuoi
                break
    print(f"So chinh phuong gan nhat: {cpGanNhat}")
    
