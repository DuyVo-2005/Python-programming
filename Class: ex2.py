class Foo:
        def printLine(self, line='Python'):
            print(line)
o1 = Foo()
o1.printLine('Java') 
class Dog:
    def walk(self):
        return "*walking*"
    def speak(self):
        return "Woof!"
class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff!"
bobo = JackRussellTerrier()
print(bobo.speak())
print(bobo.walk())
