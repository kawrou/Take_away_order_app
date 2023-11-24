class Menu:
    def __init__(self):
        self.menu_list = []
    
    def add_food(self, food):
        
        self.menu_list.append(food)
        return
    
    def show_menu(self):
        return self.menu_list