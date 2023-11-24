# Take_away_order_app
Simple Take Away Order App in Python
1. STATEMENT 
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

#Use the twilio-python package to implement this next one. You will need to use mocks too.
As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

2. DESIGN
To order - Need a menu - a list - dish : price

Order a select quantity of dishes in that menu

Receipt - shows what was order, the price, and the total price

---------------------------------------------------------------------
Menu
- Menu_items - a list containing instances of food item
- Show_all - displays all available food items (the names and price)
- Add_food? - adds instances of food to the menu?
---------------------------------------------------------------------

---------------------------------------------------------------------
Order? A peer class of menu?
- Order/Quantity? - A list or dict of food items in order
- Add items to order - acceses the menu-items and adds to order?
- Show_order - shows all items in order_list. 
---------------------------------------------------------------------

---------------------------------------------------------------------
Food Item:
- Name - string 
- Price - int?
- Availability? - Boolean?
- Make available?
- Format? - returns a string of name and price of food?
---------------------------------------------------------------------

class Menu:
    #User-facing properties:
    #   menu_items: list of instances of Food

    def __init__(self):
        #parameters:
        #   menu_items: a list containing instances of food items
        pass

    def add_food(self, food):
        #parameters:
        #   food: an instance of FoodItem
        #Side-effects:
        #   Adds the food to the menu_items property
        #Return:
        #   None
        pass
    
    def show_menu(self):
        #Returns:
        #   Shows all items on menu

class FoodItem:
    #User-facing properties:
    #   food: food item

    def __init__(self, name, price):
        # Parameters:
        #   name: string
        #   price: int
        #   availability: boolean
        pass
    def make_available(self)
        #Side-effects:
        #   Sets availability of food
        pass

class Order:
    #User-facing properties:
    # order_list: a list of food_items being ordered

    def __init__(self):
        #Parameters:
        #   order_list: a list
        pass

    def add_to_order(self):
        #Side-effects:
        #   Adds food_item to order

    def format_order(self, order):
        #Parameters:
        #   order: from order_list containing instances of the foods being ordered
        #Returns:
        #   #A nicely formated detail of the order being placed

    def show_order(self):
        format_order
        #Side_effects:
        #   Prints a nicely formatted order from the order list

    {pizza: 2, indian: 1, japanese: 3}
    "Pizza x 2, 4£, Indian x 1, 5£, Japanese x 3, 10£"
