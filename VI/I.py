class Circle:
    # default argument
    def __init__(self, radius=6):
        self.radius = radius


my_circle = Circle() #6
print(my_circle.radius)


# update instance
my_circle = Circle(8)
print(my_circle.radius) #8

# class Circles:

#     def __init__(self, radius=5, color): # This throws error
#         self.radius = radius
#         self.color = color


# my_circle = Circles(7, "Blue")
# print(my_circle.radius)
# print(my_circle.color)

#update instances
class Book:

    def __init__(self):
        self.books = []

my_books = Book()
my_books.books = ["Pride and Prejudes", "Metamorphosis"]
print(my_books.books)
#merubah elemen array
my_books.books[1] = "Romeo"
print(my_books.books)

# mini project class bacteria

class Bacteria:

    def __init__(self, x, y, shape,resistant, positive):
        self.x = x
        self.y = y
        self.shape = shape
        self.resistant = resistant
        self.positive = positive


#thes are 3 sample instances
bacteria1 = Bacteria(50, 40, "coccus", True, True)
bacteria2 = Bacteria(30, 10, "bacilus", False, True)
bacteria3 = Bacteria(40, 20, "tetrad", True, False)

# Class Atribut / global variabel
class Movie:

    # class atribute
    id = 1
    id_counter = 1
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        self.ids = Movie.id_counter

        Movie.id_counter += 1
        # Movie.id_counter = Movie.id_counter + 1


#acces class aribut
my_movie = Movie.id
print(my_movie)

#access class atribut incremental
my_movies = Movie("Juon", 1993)
print(my_movies.ids)
print(my_movies.id)

your_movies = Movie("Hercules", 1994)
print(your_movies.ids)
print(my_movies.id)

we_movies = Movie("Testing", 1994)
print(we_movies.ids)
print(my_movies.id)

#Modify Class Atribute
class Circle:

    #class Atri ute
    radius = 5

    def __init__(self, color):
        self.color = color

print(Circle.radius)

x = Circle("Blue")
x.radius = 10

print(x.radius)

# whats the value of the class attr1 after this sequences of statement?

class A:

    attr1 = 5

    def __init__(self):
        A.attr1 += 1

a1 = A()
a2 = A()
#update instance
# A.attr1 = 26
a3 = A()
print(A.attr1) # output?
#27








