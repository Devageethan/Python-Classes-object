class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print(self.name, self.age)


obj = Person()
print(obj)
obj.myfun()
