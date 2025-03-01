"""
# Name: Luis Salgado
# Date: 02/27/25
# File Purpose: Lab 05 shopping cart program
"""

# get_total_price(cart)
def get_total_price(cart):
    '''dictionary where key is the item name and value is the price, returns float of total price'''
    total = 0
    for item in cart:
        total += item[1]
    return total

# checkout_queue(*names)
def checkout_queue(*names):
    '''returns a list of names in the order they were entered'''
    return list(names)

# add_customer_cart(name, **items)
def add_customer_cart(name, **items):
    '''input the customer name  items which holds keys and price value pairs, returns nothing, only print a message that cart was added'''
    print(f"{name}'s cart has been added to the shopping list")
    
# TOFIX: write the proper implementation for this function
# lookup_cart(name)
#def lookup_cart(name):
#    '''input the customer name, returns a dictionary of the items in the cart'''
#    print(cart details here)

# remove_item(name, item)
def remove_item(name, item):
    '''input the customer name and the item to be removed, returns nothing, only print a message that item was removed'''
    print(f"{item} has been removed from {name}'s cart")

# apply_discount(name)

# add_item(name, item, price=0)

# add_item(name, item, price=0)

# sale(queue)