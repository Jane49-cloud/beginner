# class Point:
#
#     def __init__(self ,x,y):
#         self.x = x
#         self.y = y
#
#   #methods of Point Class
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# # this is an object
#
#
# point = Point()
# point.x = 10
# print(point.x)
# point.draw()
# point.move()
#
# #constructor
# # def __init__(self, x, y):
# #     self.x = x
# #     self.y = y
# #

# exercice
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, i am {person.name}")


person = Person("John Smith")
person.talk()

class Living:
    def live(self):
        print("Alive")

class Mammal(Living):
    def walk(self):
        print("walk")



class Dog(Mammal):
    pass


# inheritance
class Cat(Mammal):
    pass


dog = Dog()
dog.walk()
cat = Cat()
dog.live()
cat.live()
