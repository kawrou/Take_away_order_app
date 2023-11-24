from lib.menu import*
from unittest.mock import Mock

pizza = Mock()
pizza.name.return_value = "Pizza"
pizza.price.return_value = 5
pizza.availability = True

hot_dog = Mock()
hot_dog.name.return_value = "Hot Dog"
hot_dog.price.return_value = 3
hot_dog.availability = True

burger = Mock()
burger.name.return_value = "Burger"
burger.price.return_value = 4
burger.availability = True

"""
Given a single instance of food to be added to the menu
Food should be added to the menu_items list
show_menu should return the food_item in list
"""
def test_for_single_food_added_to_menu_list():
    new_menu = Menu()
    new_menu.add_food(pizza)
    assert new_menu.show_menu() == [pizza]



"""
Given multiple instances of food to be added to the menu
Instances of food should be added to the menu_items list if it's not already in the list
show_menu should then display all the food on the menu if it's availble to order
"""
def test_view_menu():
    #new_menu = Menu()
    #FoodItem("Pizza", £5) => name: "Pizza" price: £5
    #add_food(food_1) & add_food(food_2) gets added to menu_items list
    #show_menu() => [food_1, food_2]
    new_menu = Menu()
    new_menu.add_food(pizza)
    new_menu.add_food(hot_dog)
    new_menu.add_food(burger)
    assert new_menu.show_menu() == [pizza, hot_dog, burger]
    pass