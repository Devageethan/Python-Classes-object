class s1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"({self.name}),({self.age})"


a = s1('deva', 23)
print(a)
