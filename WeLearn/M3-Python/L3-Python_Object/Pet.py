class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_pet1 = Pet("Fido", 3)
print("My pet %s is %s years old") % (my_pet1.name, my_pet1.age)
my_pet2 = Pet("Chungus", 69)
print("My pet %s is %s years old") % (my_pet2.name, my_pet2.age)
my_pet3 = Pet("Lil dug", 420)
print("My pet %s is %s years old") % (my_pet3.name, my_pet3.age)

class Student(object):
    def __init__(self, name, age, gender, major):
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major

my_student = Student("Jorge Vasquez", 17, "Male", "Computer Science")

print("Hi my name is %s and I am %s years old. My gender is %s and I am majoring in %s") % (my_student.name, my_student.age, my_student.gender, my_student.major)

class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"
    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "lethargic"
    def move(self):
        print("> %s is eating..." % self.name)
        if self.mood:
            self.mood = "happy"
        else:
            print("> %s doesn't look too happy today." % self.name)
            self.mood = "lethargic"
my_pet = Pet("Spooky", 3, "dog")

my_pet.is_hungry = True
print("Is my pet hungry? %s" % my_pet.is_hungry)
print("How about now? %s" % my_pet.is_hungry)
print("My pet is feelings %s" % my_pet.mood)
