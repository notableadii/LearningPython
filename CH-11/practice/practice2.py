class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof! Woof!")
        
a = Dog()
a.bark()  # This will call the static method bark of the Dog class