class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class DogCat(Dog, Cat):
    pass

dog_cat = DogCat("Rex")
print(dog_cat.name)  # Rex
print(dog_cat.sound())  # Woof!
```

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class DogCat(Cat, Dog):
    pass

dog_cat = DogCat("Rex")
print(dog_cat.name)  # Rex
print(dog_cat.sound())  # Woof!
