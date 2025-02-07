class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = 100
        self.hunger = 0

    def eat(self, food_amount):
        self.hunger = max(0, self.hunger - food_amount)
        self.energy = min(100, self.energy + food_amount // 2)
        print(f"{self.name} has eaten and is less hungry now!")

    def play(self):
        if self.energy > 20:
            self.energy -= 20
            self.hunger += 15
            print(f"{self.name} is having fun playing!")
        else:
            print(f"{self.name} is too tired to play.")

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = 100
        self.hunger += 10
        print(f"{self.name} is well-rested and full of energy!")

    def bark(self):
        print(f"{self.name} barks: Woof-woof!")

    def status(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age} years")
        print(f"Energy: {self.energy}, Hunger: {self.hunger}")


# Example usage
my_dog = Dog("Izi", "Doberman", 3)
my_dog.status()
my_dog.play()
my_dog.eat(30)
my_dog.sleep()
my_dog.bark()
my_dog.status()
