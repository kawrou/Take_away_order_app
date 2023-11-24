from lib.food_item import*
from lib.menu import*
from lib.order import*


"""
Given some food to be added to the menu
Instances of food should be added to the menu_items list if it's not already in the list
show_menu should then display all the food on the menu if it's availble to order
"""
def test_view_menu():
    #new_menu = Menu()
    #FoodItem("Pizza", £5) => name: "Pizza" price: £5
    #add_food(food_1) & add_food(food_2) gets added to menu_items list
    #show_menu() => [food_1, food_2]
    new_menu = Menu()
    pizza = FoodItem("Pizza", 5)
    hot_dog = FoodItem("Hot Dog", 3)
    burger = FoodItem("Burger", 4)
    new_menu.add_food(pizza)
    new_menu.add_food(hot_dog)
    new_menu.add_food(burger)
    assert new_menu.show_menu() == [pizza, hot_dog, burger]
"""
Given a menu list filled with instances of food items
show_menu should then display all the food on the menu that is available to order
User can then choose what food to order
Order the food
And display a nicely formated list of ordered food
"""
def test_order_food():
    #new_menu = Menu()
    #add_food(food_1) & add_food(food_2) gets added to menu_items list
    #show_menu() => [food_1, food_2]
    #add_to_order adds selected food to order_list
    #show_order => "Food Item, Quantity, subtotal ... total"
    pass

