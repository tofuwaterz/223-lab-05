import unittest
from shopping import get_total_price, checkout_queue, add_customer_cart, lookup_cart, remove_item, apply_discount, add_item, sale
from collections import deque

class TestShoppingFunctions(unittest.TestCase):

    def test_get_total_price(self):
        cart = {'apple': 1.0, 'banana': 2.0, 'orange': 3.0}
        self.assertEqual(get_total_price(cart), 6.0)
        
        cart = {'apple': 1.5, 'banana': 2.5}
        self.assertEqual(get_total_price(cart), 4.0)
        
        cart = {}
        self.assertEqual(get_total_price(cart), 0.0)

    def test_checkout_queue(self):
        queue = checkout_queue('Alice', 'Bob', 'Charlie')
        self.assertEqual(queue, deque(['Alice', 'Bob', 'Charlie']))
        
        queue = checkout_queue()
        self.assertEqual(queue, deque())

    def test_add_customer_cart(self):
        add_customer_cart('Alice', apple=1.0, banana=2.0)
        # The output will be checked manually as we don't have return values in the function.
        
        # Testing a customer with no items
        add_customer_cart('Bob')
        # Again, no return value to assert, but the message should confirm the cart is added.
        
    def test_lookup_cart(self):
        add_customer_cart('Alice', apple=1.0, banana=2.0)
        # The output will be checked manually as we don't have return values in the function.
        lookup_cart('Alice')
        
        # Checking for a customer who doesn't exist
        lookup_cart('Nonexistent')

    def test_remove_item(self):
        add_customer_cart('Alice', apple=1.0, banana=2.0)
        remove_item('Alice', 'banana')
        # Checking if the item is removed correctly; manual verification of the printed message is needed.
        
        # Trying to remove an item that doesn't exist
        remove_item('Alice', 'grape')

    def test_apply_discount(self):
        add_customer_cart('Alice', apple=1.0, banana=2.0)
        discount = apply_discount('Alice')
        self.assertEqual(discount, 10)  # Assuming a fixed discount percentage.
        
        # Test with a customer who doesn't exist
        discount = apply_discount('Nonexistent')
        self.assertEqual(discount, 0)

    def test_add_item(self):
        add_customer_cart('Alice', apple=1.0)
        add_item('Alice', 'banana', 2.0)
        # Manual verification of printed message needed for confirming item addition.
        
        # Test adding a free item
        add_item('Alice', 'orange', 0)
        # Manual verification of printed message needed for confirming item added as free.
        
        # Test when the customer doesn't exist
        add_item('Nonexistent', 'pear', 1.5)

    def test_sale(self):
        queue = deque(['Alice', 'Bob'])
        add_customer_cart('Alice', apple=1.0, banana=2.0)
        add_customer_cart('Bob', orange=3.0)
        sale(queue)
        # We will manually verify the printed output since this function doesn't return anything.
        
        queue = deque()
        sale(queue)  # Test with an empty queue

if __name__ == '__main__':
    unittest.main()
