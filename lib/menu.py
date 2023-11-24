class Menu:
    def __init__(self):
        self.menu_list = []
    
    def add_food(self, food):
        if food not in self.menu_list:
            self.menu_list.append(food)
        else:
            raise Exception("Food item already in menu")
        return
    
    def show_menu(self):
        return [food for food in self.menu_list if food.availability == True]