class LunchMenu:
    '''Tracks items on the Lunch Menu'''

    def __init__(self):
        self.beverages=[]
        self.foods=[]

    def add_food(self, food):
        self.foods.append(food)
    
    def add_beverage(self, beverage):
        self.beverages.append(beverage)

    def generate(self):
        print('Foods:')
        for food in self.foods:
            print(f"- {food}")
        
        print('Beverages:')
        for beverage in self.beverages:
            print(f"- {beverage}")

if __name__ == '__main__':
    my_menu=LunchMenu()

    my_menu.add_food('Salad')
    my_menu.add_food('Soup')
    my_menu.add_food('Burger')
    my_menu.add_food('Steak')
    my_menu.add_beverage('Coffee')
    my_menu.add_beverage('Wine')
    my_menu.generate()

    veg_menu=LunchMenu()

    veg_menu.add_food('salad')
    veg_menu.add_food('veggie burger')
    veg_menu.add_food('sweet potato fries')
    veg_menu.add_food('sandwinch')
    veg_menu.add_food('black bean soup')
    print("Vegetarin Menu:")
    veg_menu.generate()

    meat_menu=LunchMenu()
    meat_menu.add_food('beef soup')
    meat_menu.add_food('chicken sandwich')
    meat_menu.add_food('steak')
    meat_menu.add_food('beef burger')
    print("Meat Menu:")
    meat_menu.generate()

