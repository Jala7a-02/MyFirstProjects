menu = {
    "pizza" : 12, 
    "soda" : 5, 
    "corn" : 6,
    "chips" : 2.6,
    "water" : 1.25,
    "tap-soda" : 2.50,
    "coca-cola" : 4,
    "wi-fi" : 5.75
}

cart = []

total = float(0)
print("----- MENU ----")
for key , value in menu.items():
    print(f"{key:10} : {value:.2f}")
print("--------------")

while True:

    cart_item = input("what would you like to order ? (q to quit)")  
    
    if cart_item == "q" :

        break

    elif menu.get(cart_item) is not None :

        cart.append(cart_item)

print("______ YOUR ORDERS ______")
for food in cart :
    total += menu.get(food)
    print(food, end=" ")
print()
print("________________")
print()




print("________ TOTAL ________")
print(f"your total is : {total:.2f}")
print("__________________")


