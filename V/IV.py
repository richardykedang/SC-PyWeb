class Pizza:
    def __init__(self, extratopping = ""):
        self.topping = "tomato sauce, chopped sausage"
        self.extratopping = extratopping

    def defaultTopping(self):
        return self.topping

    @classmethod
    def cheeseTopping(cls):
        extratopping = ", Cheese"
        extra = cls(extratopping)
        res = extra.topping + extra.extratopping
        return res


myPizza = Pizza()
print(myPizza.defaultTopping())
pizza1 = Pizza.cheeseTopping()
# print(Pizza.cheeseTopping())
print(pizza1)
