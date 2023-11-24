from lib.menu import*
from unittest.mock import Mock
import pytest

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
Given a two instance of the same food to be added to the menu
Food should only be added to the menu_items list if it's unique
Raise exception error
"""
def test_multiples_of_same_food_in_menu_list_raises_exception_error():
    new_menu = Menu()
    new_menu.add_food(pizza)
    with pytest.raises(Exception) as e:
        new_menu.add_food(pizza)
    error_message = str(e.value)
    assert error_message == "Food item already in menu"


"""
Given multiple instances of food to be added to the menu
Instances of food should be added to the menu_items list if it's not already in the list
show_menu should then display all the food on the menu
"""
def test_show_the_menu_of_3_food_items():
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

"""
Given multiple instances of food to be added to the menu
Instances of food should be added to the menu_items list if it's not already in the list
show_menu should then display all the food on the menu if it's availble to order
"""
def test_show_the_menu_only_of_items_available_to_order():
    #new_menu = Menu()
    #FoodItem("Pizza", £5) => name: "Pizza" price: £5
    #add_food(food_1) & add_food(food_2) gets added to menu_items list
    #show_menu() => [food_1, food_2]
    new_menu = Menu()
    new_menu.add_food(pizza)
    new_menu.add_food(hot_dog)
    new_menu.add_food(burger)

    chicken = Mock()
    chicken.availability.return_value = False

    new_menu.add_food(chicken)
    #new_menu.add_food.assert_called_with(chicken)
    assert new_menu.menu_list == [pizza, hot_dog, burger, chicken]
    assert new_menu.show_menu() == [pizza, hot_dog, burger]

