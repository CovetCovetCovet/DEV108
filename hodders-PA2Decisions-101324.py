#!/usr/bin/env python3

print("*** Acme Rocket Division Corporation ***")           #Title
print("\nSupporting the animation industry for 100 years and counting!!")
print("\nHi, I'm Sara. How many rockets would you like to order today?")


#while True:            #Attempted validation, but commented it out since we aren't supposed to be doing form validation yet.
rocket_qty = int(input("\nNumber of rockets: \t\t"))            #User input
    #if rocket_qty <= 0:
        #print("\nYou must enter a number greater than 0.")
    #elif rocket_qty > 0:
        #break
print("\nI can certainly help you with that.  Could you please give me your name and address?")
customer_name = (input("\nFirst and last name: \t\t"))
customer_street = (input("\nStreet address: \t\t"))
customer_city = (input("\nCity: \t\t\t\t"))
customer_state = (input("\nState (two letters): \t\t"))
customer_zip_code = str(input("\nZip code: \t\t\t"))


loyalty_member = input("\nAre you a member of our Futility Club Loyalty program (\"Y\" if yes)?\t")     #Loyalty club
if loyalty_member.upper() == "Y":
    print("\nYou'll get an AMAZING 15% loyalty bonus today!")
else:
    pass


free_gift = input("\nToday only, we're offering an appreciation gift with each order."      #Limited time gift
                  "\nWould you like a FREE Jet-Propelled Pogo Stick (enter 'P')"
                  "\nor a FREE Jar of Bumble Bees (enter 'B')?\t")
input("\nPress any key to display invoice...")


if rocket_qty >= 20:            #Bulk order calculations
    rocket_price = 68.25
elif rocket_qty >= 10 and rocket_qty <= 19:
    rocket_price = 70.00
else:
    rocket_price = 88.50


loyalty_discount = 0.15         #Base amounts
tax_percent = 0.1
shipping_cost = 112


price = (rocket_price * rocket_qty)         #Calculate standard price
if loyalty_member.upper() == "Y":
    discount_amount = price * loyalty_discount
    ext_price = price - discount_amount
else:
    discount_amount = 0
    ext_price = price


if rocket_qty < 5 and (customer_state.upper() == "CA" or customer_state.upper() == "OR"):           #Calculate shipping cost
    shipping = 0
else:
    shipping = shipping_cost * rocket_qty


tax_amount = ext_price * tax_percent            #Calculate sales tax
subtotal = ext_price + tax_amount
order_total = subtotal + shipping           #Calculate order total


formatted_rocket_price = f"${rocket_price:,.2f}"            #Formatting for invoice
formatted_price = f"${price:,.2f}"
formatted_discount_amount = f"(${discount_amount:,.2f})"
formatted_ext_price = f"${ext_price:,.2f}"
formatted_tax_amount = f"${tax_amount:,.2f}"
formatted_shipping = f"${shipping:,.2f}"
formatted_order_total = f"${order_total:,.2f}"


print("\n\n=========================================================================")          #Invoice
print("\n\n*** ACME Anvils Corporation ***")
print("\n\nCustomer Invoice")
print("\n\nSHIP TO:")
print(f"\t\t{customer_name}")
print(f"\t\t{customer_street}")
print(f"\t\t{customer_city}")
print(f"\t\t{customer_state}")
print(f"\t\t{customer_zip_code}")
print(f"\n\nQuantity:\t\t\t{rocket_qty:>10}")
print(f"Cost per rocket:\t\t{formatted_rocket_price:>10}")
print(f"Subtotal:\t\t\t{formatted_price:>10}")

if loyalty_member.upper() == "Y":
    print(f"Less 15% Futility Club:\t\t{formatted_discount_amount:>11}")
    print(f"Taxable amount:\t\t\t{formatted_ext_price:>10}")
else:
    pass

print(f"Sales Tax:\t\t\t{formatted_tax_amount:>10}")
print(f"Shipping:\t\t\t{formatted_shipping:>10}")
print("                                ___________")
print(f"\nTOTAL:\t\t\t\t{formatted_order_total:>10}")
print()

if rocket_qty < 5 and (customer_state.upper() == "CA" or customer_state.upper() == "OR"):
    print("Your order qualifies for free shipping!")
else:
    pass

if free_gift.upper() == "P":
    print("\nAlong with today's order, you'll receive a FREE JET-PROPELLED POGO STICK!")
if free_gift.upper() == "B":
    print("\nAlong with today's order, you'll receive a FREE JAR OF BUMBLE BEES!")
else:
    pass

print("\n=========================================================================")
print(f"\n\nYour total today is ${order_total:,.2f}. Thanks for shopping with Acme!")
print("\n\nAnd don't forget: Acme rockets fly farther, drop faster, and land harder than any other rocket on the market!")
input("\n\nPress any key to continue...")