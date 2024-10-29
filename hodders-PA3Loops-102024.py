#!/usr/bin/env python3

# imports
import time
import random

# greeting
def greeting():
    print("*** Acme Rocket Division Corporation ***")
    print()
    print("Supporting the animation industry for 100 years and counting!!")
    print()
    print("Hi, I'm Sara. How many rockets would you like to order today?")
    print()

# rocket qty validation
def validate_rocket_order():
    while True:
        rocket_qty = int(input("Number of rockets: \t\t"))
        print()
        if rocket_qty <= 0:
            print("Number of rockets must be a positive, whole number.")
            print()
        elif rocket_qty > 0:
            print()
            break
        
    formatted_rocket_qty = f"{rocket_qty:>25}"

    return rocket_qty, formatted_rocket_qty


# Shipping state validation
def validate_shipping_state(customer_state, permitted_states):

    return customer_state.upper() in permitted_states


# Customer data input w/ validation
def collect_customer_info():
    print("I can certainly help you with that. Could you please give me your" 
          "name and address?")
    print()
    
    while True:
        customer_name = (input("First and last name: \t\t"))
        if not customer_name:
            print()
            print("Customer name is required.")
            print()
        else:
            print()
            break
    
    customer_street = (input("Street address: \t\t"))
    print()
    customer_city = (input("City: \t\t\t\t"))
    print()

    while True:
        permitted_states =["AK", "WA", "OR", "CA", "AZ", "NM", "CO", "UT"]
        customer_state = (input("State (two letters): \t\t"))
        if not validate_shipping_state(customer_state, permitted_states):
            print()
            print(f"We do not ship to {customer_state.upper()}.")
            print()
        else:
            print()
            break

    while True:
        customer_zip_code = str(input("Zip code: \t\t\t"))
        if len(customer_zip_code) < 5 or len(customer_zip_code) > 5:
            print()
            print ("Zip code must be 5 characters long.")
            print()
        else:
            print()
            break

    return customer_name, customer_street, customer_city, customer_state, customer_zip_code


# Validation for loyalty membership with number game
def check_loyalty_member():
    number = random.randint(1,5)
    while True:
        loyalty_member = input("Are you a member of our Futility Club, the" 
                               " frequent shopper program that rewards"
                               " persistence over results? (\"Y\" if yes):\t")
        print()
        if loyalty_member.upper() == "Y":
            loyalty_member = True
            guess = int(input(f"Excellent! You’ll receive an AMAZING 15%"
                                " discount on today’s purchase! What’s more,"
                                " as a valued member of our loyalty program,"
                                " you’ll have a chance to win a bonus gift in"
                                " our exciting Members-Only Gallon of invisible"
                                " paint contest! Pick a number between 1 and"
                                " 5!\t\t"))
            if guess < 1 or guess > 5:
                print()
                print("That’s not a number between 1 and 5. What an"
                      " ultra-maroon! Still, we value your loyalty.")
                print()
                loyalty_gift = False
                break        
            elif guess != number:
                print()
                print(f"Aww, too bad. You guessed {guess}, but the secret"
                      " number was {number}. No paint. What a loser. Very"
                      " sad.")
                print()
                loyalty_gift = False
                break
            else:
                guess == number
                print()
                print(f"Woo Hoo! You guessed the secret number: {guess}. A"
                      " gallon of ACME Invisible Paint is headed your way!")
                print()
                loyalty_gift = True
                break
        elif loyalty_member.upper() == "N":
            print()
            print("What's wrong with you? That just cost you a 15% discount"
                  " and an opportunity to win some Invisible Paint. Sad.")
            print()
            loyalty_member = False
            loyalty_gift = False
            break

    return loyalty_member, loyalty_gift


# price calcuations
def calc_price(rocket_qty, loyalty_member):
    loyalty_discount = 0.15
    tax_percent = 0.0995
    shipping_cost = 99

    if rocket_qty >= 20:
        rocket_price = 67.99
    elif rocket_qty >= 10 and rocket_qty <= 19:
        rocket_price = 72.35
    else:
        rocket_price = 80.00
    
    price = rocket_price * rocket_qty

    if loyalty_member == True:
        discount_amount = price * loyalty_discount
        subtotal = price - discount_amount
    else:
        discount_amount = 0
        subtotal = price
    
    shipping = shipping_cost * rocket_qty
    tax_amount = subtotal * tax_percent
    subtotal = subtotal + tax_amount
    order_total = subtotal + shipping

    formatted_rocket_price = f"${rocket_price:>21,.2f}"
    formatted_price = f"${price:>25,.2f}"
    formatted_discount_amount = f"(${discount_amount:>21,.2f})"
    formatted_subtotal = f"${subtotal:>25,.2f}"
    formatted_tax_amount = f"${tax_amount:>25,.2f}"
    formatted_shipping = f"${shipping:>25,.2f}"
    formatted_order_total = f"${order_total:>30,.2f}"

    return order_total, formatted_rocket_price, formatted_price, \
           formatted_discount_amount, formatted_subtotal, \
           formatted_tax_amount, formatted_shipping, formatted_order_total


# invoice to print
def print_invoice(formatted_rocket_qty, customer_name, customer_street, 
                  customer_city, customer_state, customer_zip_code, 
                  loyalty_member, loyalty_gift, order_total, 
                  formatted_rocket_price, formatted_price, 
                  formatted_discount_amount, formatted_subtotal, 
                  formatted_tax_amount, formatted_shipping, 
                  formatted_order_total):
    print(input("Press any key to display invoice..."))
    print()
    print()
    print("=================================================================")
    print()
    print()
    print("*** Acme Rocket Division Corporation ***")
    print()
    print()
    print("Customer Invoice")
    print()
    print()
    print("SHIP TO:")
    print(f"\t\t {customer_name}")
    print(f"\t\t{customer_street}")
    print(f"\t\t{customer_city}")
    print(f"\t\t{customer_state}")
    print(f"\t\t{customer_zip_code}")
    print()
    print()
    print(f"Quantity: {formatted_rocket_qty}")
    print(f"Cost per rocket: {formatted_rocket_price}")
    print(f"Subtotal: {formatted_price}")

    if loyalty_member == True:
        print(f"Less 15% Futility Club: {formatted_discount_amount}")
        print(f"Taxable amount: {formatted_subtotal}")
    else:
        pass

    print(f"Sales Tax: {formatted_tax_amount}")
    print(f"Shipping: {formatted_shipping}")
    print("                                ___________")
    print()
    print(f"TOTAL: {formatted_order_total}")
    print()
    print()

    if loyalty_gift == True:
        print("And congratulations on winning FREE Invisible Paint!!!")
        print()
    else:
        pass

    print("=================================================================")
    print()
    print()
    print(f"Your total today is ${order_total}. Thanks for shopping with"
          " Acme!")
    print()
    print()
    print("And don't forget: Acme rockets fly farther, drop faster, and land"
          " harder than any other rocket on the market!")
    print()
    print()


# countdown w/ alarm sound
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    else:
        import winsound
        duration = 500
        freq = 440
        winsound.Beep(freq, duration)


# main
def main():
    again = "Y"
    while again.upper() == "N":
        print()
        print(input("Press any key to end program..."))
        print()
        break
    else:
        greeting()

        rocket_qty, formatted_rocket_qty = validate_rocket_order()

        customer_name, customer_street, customer_city, customer_state, customer_zip_code = collect_customer_info()
        
        loyalty_member, loyalty_gift = check_loyalty_member()

        order_total, formatted_rocket_price, formatted_price, formatted_discount_amount, formatted_subtotal, formatted_tax_amount, formatted_shipping, formatted_order_total = calc_price(rocket_qty, loyalty_member)

        print_invoice(formatted_rocket_qty, customer_name, customer_street, customer_city, customer_state, customer_zip_code, loyalty_member, loyalty_gift, order_total, formatted_rocket_price, formatted_price, formatted_discount_amount, formatted_subtotal, formatted_tax_amount, formatted_shipping, formatted_order_total)
        
        print()
        again = input("Ready to take another order?")
        print()
        countdown(3)
        print()
        print("******************** NEW ORDER ********************")
        print()


if __name__ == "__main__":
    main()