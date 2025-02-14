class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Hero(Person):
    def __init__(self, name, age, superpower):
        super().__init__(name, age)
        self.superpower = superpower

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Superpower: {self.superpower}"

person = Person("Tony Stark", 25)
hero = Hero("Bruce Wayne", 35, "Intellect")

print(person)
print(hero)
