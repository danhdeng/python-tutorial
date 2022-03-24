import lunch_menu

cafe_menu=lunch_menu.LunchMenu()
cafe_menu.add_food("Sandwich")
cafe_menu.add_food("bagel")
cafe_menu.add_beverage('coffee')
cafe_menu.add_beverage('tea')

print("The Cafe Menu:")
cafe_menu.generate();
