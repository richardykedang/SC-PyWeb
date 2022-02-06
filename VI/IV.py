# Decorators
# sama seperti getter dan setter cuma di persingkat saja penulisannya dgn decorator menggunakan symbol @

class Movie:

    def __init__(self, title, rating):
        self._rating = rating
        self. _title = title

    #getter
    @property
    def rating(self):
        return self._rating

    #setter
    @rating.setter
    def rating(self, new_rating):
        print("Calling the getter")
        if 1.0 <= new_rating <= 5.0:
            return self._rating
        else:
            print("Please enter a valid rating")

favorite_movie = Movie("Titanic", 4.3)
print(favorite_movie.rating)

favorite_movie.rating = 4.5
print(favorite_movie.rating)

favorite_movie.rating = 5.5 # Invalid
print(favorite_movie.rating)

# 2 List
class Backpack:

    def __init__(self):
        self._item = []

    @property
    def items(self):
        return self._item

    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._item = new_items
        else:
            print("Please Enter a valid list")

my_backpack = Backpack()
print(my_backpack.items) # []

my_backpack.items = ["Bottle", "Sleeping Bag"]
print(my_backpack.items)

my_backpack.items = "Hello world" # invalid value
print(my_backpack.items)


