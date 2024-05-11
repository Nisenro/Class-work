'''
Habbo Hotel has requested you to develop a checkout system for their new Hotel Bar. They requested the following functionality:

The user should be prompted with the following menu and prices (you may use a multiline string to print this, read more here):

1. Habbeer ($3.50)
2. Wine ($4.00)
3. Java Coffee ($2.50)
4. Apple Juice ($6.00)
5. Root Access Beer ($1.75)
The user is asked what they want to order, they should input the numbers they want to order. They can input multiple items, see:

Please write down your order: 1154
The above would be an order of two Habbeers, a Root Access Beer and an Apple Juice.

Loop through the inputted string and calculate the total price of the order by adding the individual prices. You can easily loop through a string by character using for character in string:.

Now, in a function defined as add_percentage(price, percentage=15) add the given tax to the given price and return that number. In this case, percentage has a default value of 15 and thus does not have to be given as an argument when calling the function. You may be able to re-use this function in the next step. The default tax for the Habbo Bar is 15.

Then, in a function called add_tip(price), ask the user what percentage of the total price (including tax) they want to give as a tip using input(), add this percentage to the price and return:

How much tip would you like to give? 15
Use input validation in this step: the number has to be a positive integer. Use a while-loop to continuously ask the user for input and only break if the input is correct.

Finally, print out the total price to the customer of Habbo Bar (round to two decimals):

Total price: $19.51
Write this all in a script called checkout_system.py, which should call a main() function from the if __name__ == "__main__": block that calls all functions as needed. Next to the main() function, you are required to implement at least the other two functions mentioned above, but are encouraged to split up your implementation in as many (logical) subtasks as possible.

'''
def display_menu():
    menu = ''' 1. Habbeer ($3.50)
    2. Wine ($4.00)
    3. Java Coffee ($2.50)
    4. Apple Juice ($6.00)
    5. Root Access Beer ($1.75)
    '''
    print(menu)

def get_price(item):
    prices = {
        '1': 3.50,
        '2': 4.00,
        '3': 2.50,
        '4': 6.00,
        '5': 1.75 
    }
    return prices.get(item, 0)

def get_order():
    order = input("Please write down your order: ")
    return order

def calculate_total_price(order):
    total_price = 0
    for item in order:
        price = get_price(item)
        total_price += price
    return total_price

def add_percentage(price, percentage=15):
    total_price_plus_tax = price + (price * percentage / 100)
    return total_price_plus_tax

def add_tip(total_price_plus_tax):
    while True:
        tip_input = input("How much tip would you like to give? ")
        if tip_input.isdigit() and int(tip_input) > 0:
            tip_added = int(tip_input) + total_price_plus_tax
        return tip_added
    
def print_total_price(tip_added):
    print("Total price: $", "{:.2f}".format(tip_added))

def main():
    display_menu()
    order = get_order()
    total_price = calculate_total_price(order)
    total_price_plus_tax = add_percentage(total_price)
    tip_added = add_tip(total_price_plus_tax)
    print_total_price(tip_added)

if __name__ == "__main__":
    main()