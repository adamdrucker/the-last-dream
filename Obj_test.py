class Person:
    def __init__(self, name, age, gender, race, height, weight, origin):
        self.name = name
        self.age = age
        self.gander = gender
        self.race = race
        self.height = height
        self.weight = weight
        self.origin = origin

    def wave(self):
        print(self.name + " waves!")

    def dob(self):
        print(self.name + " is " + str(self.age) + " years old, which means he was born in " +
              str(2020 - self.age) + ".")

    def scale(self):
        print(self.name + " steps on the scale and sees their weight as " + str(self.weight) + ".")

    def home_country(self):
        print(self.name + " is from " + self.origin + ".")


person1 = Person("Adam", 33, "male", "caucasian", 67, 209, "USA")
person1.wave()
person1.dob()
person1.scale()
person1.home_country()

person2 = Person("Hiro", 25, "male", "asian", 64, 166, "Japan")
person2.dob()
person2.home_country()

if person1.age > person2.age:
    print(f"{person1.name} is older than {person2.name}!")
else:
    print(f"{person2.name} is older!")