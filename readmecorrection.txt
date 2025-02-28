# Lab 5: Grocery Shopping

## Instruction:
1. Create a module `shopping.py`
Initialize an empty dictionary call cart
cart = {}

with the following functions:
get_total_price(cart)
Input: A dictionary cart where keys are item names (strings) and values are prices (floats/integers).
Returns: A float representing the total price of all items in the cart.

checkout_queue(*names)
Input: Any number of string arguments representing customer names.
Returns: A deque containing the names in the order they were received.

add_customer_cart(name, **items)
Input:
name (string): Customer's name.
items (keyword arguments): Item names as keys (strings) and their prices as values (floats/integers).
Returns: Nothing (None). Prints a message confirming the cart has been added.

lookup_cart(name)
Input: name (string) – Customer's name.
Returns: Nothing (None). Prints the cart details, including items, their prices, and the total price.

remove_item(name, item)
Input:
name (string): Customer's name.
item (string): Item to be removed.
Returns: Nothing (None). Prints a confirmation if the item is removed or a message if the item is not found.

apply_discount(name)
this function will take in one positional arguments `name`. Apply 10% discount if any conditions met
their name length is divisible by 3, OR the first letter is a vowel, . Print out their name and the discount they get. Return the discount percentage.
Input: name (string) – Customer's name.
Returns: An integer representing the total discount percentage applied. Also prints the customer's name and discount applied.

add_item(name, item, price=0)
Input:
name (string): Customer's name.
item (string): Item name.
price (float, default=0): Price of the item.
Returns: Nothing (None). Prints a confirmation message. If the item is free, it notifies the user. If the customer is not found, it prints "Name not found".

sale(queue)
Input: A deque containing customer names.
Returns: Nothing (None). Processes each customer in the queue, applies discounts if applicable, prints the cart details, and displays messages until the queue is empty.

 


2. Create main.py and import all the functions to show they are working