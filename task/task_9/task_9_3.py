# Create hierarchy out of birds.
# Implement 4 classes:
# * Birds class with an attribute "name" and methods "fly" and "walk".
# * flying bird class with same attribute "name" and with the same methods.
# Implement the method "eat" which will describe it's typical ration.
# * nonflying bird class with same characteristics but which obviously will not
# have the "fly".
# Add same "eat" method but with other implementation regarding the
# swimming bird tastes.
# * a bird class which can do all of it: walk, fly, swim and eat.
#  But be careful which "eat" method you inherit.
#  Implement str() function call for each class. Example:
# ```python
#   >>> b = Bird("Any")
#  >>> b.walk()
#  "Any bird can walk"
#  p = Penguin("Penguin")
#  >> p.swim()
#  "Penguin bird can swim"
#  >>> p.fly()
#  AttributeError: 'Penguin' object has no attribute 'fly'
#  >>> p.eat()
#  "It eats mostly fish"
#  c = Canary("Canary")
#  >>> str(c)
#  "Canary can walk and fly"
#  >>> c.eat()
#  "It eats mostly grains"
#  s = SeaGull("Gull")
#  >>> str(s)
#  "Gull bird can walk, swim and fly"
#  >>> s.eat()
#  "It eats fish"
# ```
# Have a look at __mro__ method of your last class.

class Birds:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f'{self.name} is flying.'

    def walk(self):
        return f'{self.name} is walking.'

    def eat(self):
        return f'{self.name} eats various types of food.'

    def __str__(self):
        return f'{self.name} is a bird.'


class FlyingBird(Birds):
    def eat(self):
        return f'{self.name} eats insects and small animals.'

    def __str__(self):
        return f'{self.name} is a flying bird.'


class NonFlyingBird(Birds):
    def eat(self):
        return f'{self.name} eats fish and aquatic plants.'

    def __str__(self):
        return f'{self.name} is a non-flying bird.'


class AquaticBird(Birds):
    def swim(self):
        return f'{self.name} is swimming.'

    def eat(self):
        return f'{self.name} eats fish and other aquatic animals.'

    def __str__(self):
        return f'{self.name} is an aquatic bird.'


class HybridBird(FlyingBird, AquaticBird):
    def __str__(self):
        return f'{self.name} is a hybrid bird that can fly and swim.'


bird1 = Birds('Sparrow')
print(bird1.fly())
print(bird1.walk())
print(bird1.eat())
print(bird1)
print('\n')


bird2 = FlyingBird('Eagle')
print(bird2.fly())
print(bird2.walk())
print(bird2.eat())
print(bird2)
print('\n')


bird3 = NonFlyingBird('Penguin')
print(bird3.walk())
print(bird3.eat())
print(bird3)
print('\n')


bird4 = AquaticBird('Duck')
print(bird4.swim())
print(bird4.eat())
print(bird4)
print('\n')


bird5 = HybridBird('Seagull')
print(bird5.fly())
print(bird5.swim())
print(bird5.eat())
print(bird5)
print('\n')


