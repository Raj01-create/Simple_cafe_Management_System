menu={
    'pizza':40,
    'burger':30,
    'coldrink':20,
    'sandwitch':35,
    'coffee':20
}


print("welocme to python cafe...")
   
print('pizza: Rs40\nburger: Rs30\ncoldrink: Rs20\nsandwitch: Rs35\ncoffee: Rs20')

print("select your order from menu please")
order_total =0

item_1=input("please enter your order: ")

if item_1 in menu:
        order_total +=menu[item_1]
        print(f"{item_1} is added to your order ")
else:
        print("the item is not in menu please choose acording to menu ")


anathor =input("you want any other thing to order ? Yes/no ")
if anathor== "Yes":
   item_1=input("please enter your order: ")
   if item_1 in menu:
        order_total +=menu[item_1]
        print(f"{item_1} is added to your order ") 
   else: 
      print("thank you...")
   
last=input("anythings to add or remove from your order ? Yes/no ")
if last == "Yes":
        ot=input("Add/Remove :")
        if ot=="Add":
            item_1=input("please enter your order: ")
            if item_1 in menu:
                order_total +=menu[item_1]
                print(f"{item_1} is added to your order ")
            else:
                print("the item is not in menu please choose acording to menu ")
        else:
            item_1=input("Please enter what you want to remove ")
            order_total -=menu[item_1]
            print(f"{item_1} is remove from your order ")
else:
     print("thank you.... ")

print(f"\nBill : you have to pay Rs.{order_total}")
