from lib.food_item import *

"""
Given a name of a food as a string and price of that food as an int
The class parameters should be initialized with those arguments. 
"""

def test_food_item_parameters_initialized():
    Pizza = FoodItem("Pizza", 5)
    assert Pizza.food_name == "Pizza"
    assert Pizza.food_price == 5

