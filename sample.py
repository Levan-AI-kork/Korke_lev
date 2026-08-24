# davemate dadsaaad d
# int()
#
# print(type(5))

# class MyClass:
#     pass
#
# x = MyClass()
# print(x, type(x))

new_str = "hdashd ;asjdh"
print(type(new_str), new_str.upper())

class Car:

    wheel = 54

    def __init__(self, name_1, color_test, publish_year, sichqare, karebi=4):
        self.name = name_1
        self.color = color_test
        self.year = publish_year
        self.kari = karebi
        self._protected_attr = "daculi var"
        self.__sichqaris_kolofi = sichqare

    def display_info(self):
        print(f"manqanis saxeli {self.name}, manqannis  feri: {self.color}, gamoshvebis weli {self.year}, {self.wheel}")

    def go(self):
        print(f"{self.name} gadis 200 kilometres")

    def count_door(self, x, y, z):
        print(x, y, z)
        return self.kari

    @property
    def sichqaris_kolofi(self):
        return self.__sichqaris_kolofi



my_car = Car("Toyota", "Tetri", 2001, "sichqare")
my_car2 = Car("BMW", "Green", 2020, "meqanika", 2)
my_car3 = Car(name_1="Mercedes", color_test="Shavi", publish_year=2010, sichqare="tiptroniki")


my_car.display_info()
my_car.go()

print(my_car.name, my_car2.name, my_car3.name)
print(my_car.wheel, my_car2.wheel, my_car3.wheel)



print(my_car2.count_door(1, 2, "jdsakhd "))
print(my_car.count_door(32, 40, "87"))
print(my_car3.count_door([1, 32, 324 ], {"a": 12}, (1, 2, 3)))

# new_car1 = Car()
# new_car2 = Car()
# new_car3 = Car()
# new_car4 = Car()
# print(new_car1, type(new_car1))
#
# new_car1.name = "BMW"
# new_car1.color = "Green"
# new_car1.year = 2020
#
#
# print(new_car1)
# print(new_car1.name)
# print(new_car1.color)


my_car.color= "UIIUIUIUIU"
print(my_car.color)
print(my_car2._protected_attr)
my_car2._protected_attr = "sheicvala"
print(my_car2._protected_attr)

my_car.__sichqaris_kolofi = "shevcvale"
print(my_car.__sichqaris_kolofi)


print(my_car.sichqaris_kolofi)
my_car.sichqaris_kolofi = "sjahdkhas dkhaskd askjdh"
print(my_car.sichqaris_kolofi)