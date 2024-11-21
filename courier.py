import math  # Imports the math functions into python file

package_price = None

while package_price is None:
    try:
        package_price = float(input("Please enter the price of your package: "))  #Requests input from user
        print(" ")
    except ValueError:
        print("Please enter a numerical value!")
        print(" ")
delivery_distance = None

while delivery_distance is None:
    try:
        delivery_distance = float(input("Please enter the delivery distance in Kilometres (km): "))# Requests input from user
        print(" ")
    except ValueError:
        print("Please enter a numerical value")
        print(" ")


air_travel = 0.36  # These declare values for each of the different variables used in this system
freight_travel = 0.25
full_insurance = 50.00
limit_insurance = 25.00
gift_levy = 15.00
priority_delivery = 100.00
std_delivery = 20.00
print("For any letter inputs of 'y' or 'n', please use lower case, thankyou!")
print(" ")

while True:
    travel_method = input("For air travel (y), for freight travel (n): ").lower()  # Requests input from user
    if travel_method == "y":  # if the letter 'y' is entered, the next condition will execute
        air_travel_yes = round(delivery_distance * air_travel, 2)  # value for delivery distance x value of air travel cost
        total_price_A = package_price + air_travel_yes  # total_A = price of package + air travel cost
        print(f"You have selected air travel, which will cost: <R{air_travel_yes}>")
        travel_method_str = "Air Travel"
        # Prints the string above with the cost of the air travel
        print(" ")
        break
    elif travel_method == "n":  # If the letter 'n' is entered, the next condition will execute
        freight_travel_yes = round(delivery_distance * freight_travel, 2)  #Value for delivery distance x value off freight
        total_price_A = package_price + freight_travel_yes  #total_A = price of package + freight travel cost
        print(f"You have selected freight travel, which will cost: <R{freight_travel_yes}>")
        travel_method_str = "Freight travel"
        # Prints string above with the cost of the freight travel
        print(" ")
        break
    else:
        print("Please choose a correct option") # Executes when any value other than 'y' or 'n' is entered

while True:
    insurance_type = input("For full insurance (y), for limited insurance (n): ").lower() # Requests input from user
    if insurance_type == "y": # if the letter 'y' is entered, the next condition will execute
        total_price_B = total_price_A + full_insurance  # total_B = total_A + full insurance cost
        print(f"You have selected full insurance, which will cost: <R{full_insurance}>")
        insurance_type_str = "Full Insurance"
        # Prints string above with the cost of the full insurance choice
        print(" ")
        break
    elif insurance_type == "n":  # If the letter 'n' is entered, the next condition will execute
        total_price_B = total_price_A + limit_insurance  # total_B = total_A + limited insurance cost
        print(f"You have selected limited insurance, which will cost: <R{limit_insurance}>")
        insurance_type_str = "Limited Insurance"
        # Prints string above with the cost of the limited insurance choice
        print(" ")
        break
    else:
        print("Please choose a correct option")  # Executes when any value other than 'y' or 'n' is entered

while True:
    gift = input("Would you like gift wrap service? Yes (y), No (n): ").lower() # Requests input from user
    if gift == "y":  # if the letter 'y' is entered, the next condition will execute
        total_price_C = total_price_B + gift_levy  #total_C = total_B + gift cost
        print(f"You have selected the gift wrap option, which will cost: <R{gift_levy}>")
        gift_levy_str = "Yes"
        # Prints string above with the cost of the gift option
        print(" ")
        break
    elif gift == "n":  # If the letter 'n' is entered, the next condition will execute
        total_price_C = total_price_B + 0 # Total_C = total_B + zero because the no gift option is free
        print("You have selected no gift wrap which is free")
        gift_levy_str = "No"
        # Prints string above with no adition because of it being zero or free
        print(" ")
        break
    else:
        print("Please choose a correct option")  # Executes when any value other than 'y' or 'n' is entered

while True:
    delivery_method = input("For priority delivery (y) and for standard delivery (n): ").lower()
    #Requests input from user
    if delivery_method == "y":  # if the letter 'y' is entered, the next condition will execute
        total_price_D = total_price_C + priority_delivery  # total_D = Total_C + priority delivery cost
        print(f"You have selected priority delivery, which will cost: <R{priority_delivery}>")
        # Prints string above with the cost of the priority delivery fee
        print(" ")
        break
    elif delivery_method == "n":  # If the letter 'n' is entered, the next condition will execute
        total_price_D = total_price_C + std_delivery # total_D = total_C + standard delivery fee (this is the final total)
        print(f"You have selected standard delivery, which will cost: <R{std_delivery}>")
        # Prints string above with the cost of the standard delivery fee
        print(" ")
        break
    else:
        print("Please choose a correct option")  # Executes when any value other than 'y' or 'n' is entered

print(" ")
print("Delivery Summary...")
print(" ")
print(f"Travel method: <{travel_method_str}>")
print(f"Insurance type: <{insurance_type_str}>")
print(f"Gift wrap service?: <{gift_levy_str}>")
print(f"The total price to pay today is: <R{total_price_D}>")
print(" ")
print("....thankyou for shipping with us!")
# Prints the string above including the total price of all fees added together!


