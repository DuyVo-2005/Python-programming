class A:
    def __init__(self, x = 2, y = 3):
        self.x = x
        self.y = y
    def __str__(self):
        return "A"
    def __eq__(self, num ):
        return self.x * self.y == num.x * num.y#?
def main():
    a = A(1, 2)
    b = A(2, 1)
    print(a == b)
main()
