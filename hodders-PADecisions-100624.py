#!/usr/bin/env python3

# Title
print("*** Acme Rocket Division ***")
print("\nSupporting the animation industry since 1949!!")
print("\nHi, I'm Sara. How many rockets would you like to order today?")

# User input
rocketQty = int(input("\nNumber of rockets: \t\t"))
print("\nI can certainly help you with that.  Could you please give me your name and address?")
customerName = (input("\nFirst and last name: \t\t"))
customerAddressStreet = (input("\nStreet address: \t\t"))
customerAddressCity = (input("\nCity: \t\t\t\t"))
customerAddressState = (input("\nState (two letters): \t\t"))
customerAddressZipCode = str(input("\nZip code: \t\t\t"))
input("\nPress any key to display invoice...")

# Cost data
rocketPrice = round(88.50, 2)
taxPercent = float(0.095)
subtotal = round(rocketQty * rocketPrice, 2)
taxAmount = round(subtotal * taxPercent, 2)
orderTotal = round(subtotal + taxAmount, 2)

# Invoice
print("\n\n==========================================")
print("\n\n*** ACME Rocket Division ***")
print("\n\nCustomer Invoice")
print("\n\nSHIP TO:")
print(f"\t\t{customerName}")
print(f"\t\t{customerAddressStreet}")
print(f"\t\t{customerAddressCity}")
print(f"\t\t{customerAddressState}")
print(f"\t\t{customerAddressZipCode}")
print(f"\n\nQuantity ordered:\t\t{rocketQty}")
print(f"\nCost per rocket:\t\t${rocketPrice}")
print(f"\nSubtotal:\t\t\t${subtotal}")
print(f"\nSales Tax:\t\t\t{taxAmount}")
print("\n__________________________________________________")
print(f"\n\nTOTAL:\t\t\t\t${orderTotal}")
print("\n\n==========================================")
print(f"\n\nYour total today is {orderTotal}. Thanks for shopping with Acme!")
print("\n\nAnd don't forget: Acme rockets fly farther, drop faster, and land harder than any other rocket on the market!")
input("\n\nPress any key to end program...")