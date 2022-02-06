# #public and non public atribute
# from turtle import color


# class Car:

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# my_car = Car("Porsche", "91Carera", 2020)
# print(my_car.year) # 2020

# my_car.year = 2500
# print(my_car.year) # 2500

# # Non public atrobute / private = atribut yg tidak bisa di akses atau modified diluar dari kelasnya sendiri
# # Getter
# class Movie:

#     def __init__(self, title, rating):
#         self._title = title
#         self.rating = rating

#         #getter method def get__title
#     def get_title(self):
#         return self._title

# #create instance movies
# my_movies = Movie("GodFather", 4.8)
# # print(my_movies._title)
# print(my_movies.get_title())

# # Setter # update value non public atribute
# class Dog:

#     def __init__(self, name, age):
#         self._name = name
#         self.age = age

#     #getter
#     def get_name(self):
#         return self._name

#     #setter = def set_namaatribute
#     def set_name(self, new_name):
#         if isinstance(new_name, str) and new_name.isalpha():
#             self._name = new_name
#         else:
#             print("Please Enter a vvalid name")

# my_dog = Dog("Nora", 4)
# print("My dog name is : ", my_dog.get_name())

# my_dog.set_name("Norita")
# print("My dog new name is : ", my_dog.get_name())

# # Negative case
# my_dog.set_name(457)
# print("My dog new name is : ", my_dog.get_name())

# my_dog.set_name("Norita123")
# print("My dog new name is : ", my_dog.get_name())

# my_dog.set_name("Nobita")
# print("My dog new name is : ", my_dog.get_name())

# # getter setter list non public
# class Backpack:

#     def __init__(self):
#         self._item = []

#     #getter
#     def get_item(self):
#         return self._item

#     #setter
#     def set_item(self, new_items):
#         if isinstance(new_items, list):
#             self._item = new_items
#         else:
#             print("Please enter a valid list of item")

# # instances
# my_backpack = Backpack()
# print(my_backpack.get_item()) # []
# my_backpack.set_item(["kaos", "celana"])
# print(my_backpack.get_item())

# #negative case
# my_backpack.set_item("handuk")
# print(my_backpack.get_item())

# # getter and setter float non public
# class Circle:

#     def __init__(self, radius):
#         self._radius = radius

#     def get_radius(self):
#         return self._radius

#     def set_radius(self, new_radius):
#         if isinstance(new_radius, float) and new_radius > 0 :
#             self._radius = new_radius
#         else:
#             print("Please enter a valid value for the radius")

# my_circle = Circle(23.3)
# print(my_circle.get_radius())
# my_circle.set_radius(20)
# print(my_circle.get_radius())

# 4
class Circle:

    VALID_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0 :
            self._radius = new_radius
        else:
            print("Please enter a valid value for the radius")

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Please enter a valid color")

    color = property(get_color, set_color)

my_circle = Circle(10.0, "Blue")

#Radius
print("radius : ", my_circle.radius)
my_circle.radius = 16.0 # untuk modified / update nilai
print(my_circle.radius)

#Color
print(my_circle.color)
my_circle.color = "Red"
print(my_circle.color)

my_circle.color = "White"
print(my_circle.color)




