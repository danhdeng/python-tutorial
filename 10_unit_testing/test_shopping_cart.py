import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    Inventory ={
        'apple':0.89,
        'orange':0.79,
        'potato':1.29,
        'banana':0.67,
    }

    def test_add_item_given_new_item_adds_new_item_to_cart(self):
        shopping_cart_unittest=ShoppingCart(self.Inventory)
        shopping_cart_unittest.add_item('apple', 8)
        self.assertEqual(shopping_cart_unittest.items_in_cart, {'apple': 8})

    def test_add_item_given_multiple_new_item_adds_new_item_to_cart(self):
        shopping_cart_unittest=ShoppingCart(self.Inventory)
        shopping_cart_unittest.add_item('apple', 8)
        shopping_cart_unittest.add_item('orange', 1)
        shopping_cart_unittest.add_item('banana', 2)
        self.assertEqual(shopping_cart_unittest.items_in_cart, {'apple': 8, 'orange': 1, 'banana': 2})

    def test_add_item_given_item_not_in_databse_not_update_cart(self):
        shopping_cart_unittest=ShoppingCart(self.Inventory)
        shopping_cart_unittest.add_item('apple', 8)
        shopping_cart_unittest.add_item('kiwi', 8)
        shopping_cart_unittest.add_item('tomato', 8)
        self.assertEqual(shopping_cart_unittest.items_in_cart, {'apple': 8})

    def test_add_item_given_existing_item_to_update_cart(self):
        shopping_cart_unittest=ShoppingCart(self.Inventory)
        shopping_cart_unittest.add_item('apple', 8)
        shopping_cart_unittest.add_item('apple', 8)
        shopping_cart_unittest.add_item('apple', 23)
        self.assertEqual(shopping_cart_unittest.items_in_cart, {'apple': 39})

    def test_add_item_given_negative_item_to_not_update_cart(self):
        shopping_cart_unittest=ShoppingCart(self.Inventory)
        shopping_cart_unittest.add_item('apple', 8)
        shopping_cart_unittest.add_item('apple', -8)
        shopping_cart_unittest.add_item('apple', 23)
        self.assertEqual(shopping_cart_unittest.items_in_cart, {'apple': 31})

    def test_calculate_total_given_added_item_sets_total_cost(self):
        shopping_cart_unittest=ShoppingCart(self.Inventory)
        shopping_cart_unittest.add_item('apple',10)
        shopping_cart_unittest.add_item('orange',2)
        total=shopping_cart_unittest.calculate_total()
        self.assertEqual(total, 10.48)

if __name__ == '__main__':
    unittest.main()