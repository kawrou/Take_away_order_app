from lib.food_item import *
import pytest

"""
Given a name of a food as a string and price of that food as an int
The class parameters should be initialized with those arguments. 
"""

def test_food_item_parameters_initialized():
    pizza = FoodItem("Pizza", 5)
    assert pizza.name == "Pizza"
    assert pizza.price == 5

def test_food_item_parameters_initialized_2():
    hot_dog = FoodItem("Hot Dog", 3)
    assert hot_dog.name == "Hot Dog"
    assert hot_dog.price == 3

"""
Given a name of a food as a string and price of that food as an int
The availability of that food should be initialized as True
"""

def test_food_item_is_available():
    pizza = FoodItem("Pizza", 5)
    assert pizza.availability == True

"""
Given a name of a food as a string and price of that food as an int
When the user makes the food unavailble
The availability should return False
"""

def test_food_item_is_made_unavailable():
    pizza = FoodItem("Pizza", 5)
    pizza.make_unavailable()
    assert pizza.availability == False

"""
Given a name of a food as a string and price of that food as an int
When the user makes the food unavailble, they should be able to make it available again. 
The availability should return True
"""

def test_food_item_is_made_available():
    pizza = FoodItem("Pizza", 5)
    pizza.make_unavailable()
    pizza.make_available()
    assert pizza.availability == True

"""
If the item is already availble, 
Should raise error code "Item already made available"
"""
def test_error_for_already_available_food():
    pizza = FoodItem("Pizza", 5)
    with pytest.raises(Exception) as e:
        pizza.make_available()
    error_message = str(e.value)
    assert error_message == "Item already available"

"""
If the item is already unavailable, 
Should raise error code "Item already made unavailable"
"""
def test_error_for_already_unavailable_food():
    pizza = FoodItem("Pizza", 5)
    pizza.make_unavailable()
    with pytest.raises(Exception) as e:
        pizza.make_unavailable()
    error_message = str(e.value)
    assert error_message == "Item already unavailable"
