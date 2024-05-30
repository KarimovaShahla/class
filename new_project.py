import os
import time


class Person:
    def __init__(self, name, age, nationality, gender) -> None:
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
        self.houses = [ ]

    def buy_house(self, house):
        self.houses.append(house)
    
    def get_houses(self):
        return [house.get_information() for house in self.houses]
    
    def get_peopple(self):
        return f"Name: {self.name}, Age: {self.age}, Nationality: {self.nationality}, Gender: {self.gender}"
    

class House:
    def __init__(self, adress, area, price, owner) -> None:
        self.adress = adress
        self.area = area
        self.price = price
        self.owner = owner
        

    def get_information(self):
        return f"Adress: {self.adress}, Area: {self.area} m², Price: {self.price} $, Owner: {self.owner}"
    
    def check_age(self):
        return len(list(filter(lambda h: h.age >= 18, self.age)))
    
    
person_1 = Person("Alina", 26, "azerbaijani", "female")
person_2 = Person("Kanan", 45, "arabian", "male")

house_1 = House("Baku", 150, 500000, "Minur")
house_2 = House("Dubai", 100, 8000000, "El Habib")
house_3 = House("Russia", 80, 300000, "Aleks")


person_1.buy_house(house_1)
person_1.buy_house(house_2)
person_2.buy_house(house_3)

print("\033[95mWelcomeeeee😊\033[0m")
time.sleep(1)
print("\033[96mOur houses are....\033[0m")
print(house_1.get_information())
time.sleep(1)
print(house_2.get_information())
time.sleep(1)
print(house_3.get_information())
time.sleep(1)
print("\033[94mOur people are....\033[0m")
time.sleep(1)
print(person_1.get_peopple())
time.sleep(1)
print(person_2.get_peopple())
time.sleep(2)
os.system("cls")
print(f"{person_1.name}'s houses: {person_1.get_houses()}")
print(f"{person_2.name}'s houses: {person_2.get_houses()}")