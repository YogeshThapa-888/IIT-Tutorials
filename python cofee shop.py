print("Welcome to the python Cofee Shop")

C_name= input("What is your name? ")

print("Our menu items\n")

P_coffee = 3.75
P_latte = 4.25
P_espresso = 4.75
P_mocha = 5.75
print("Coffee: $" + str(P_coffee))
print("Latte: $" + str(P_latte))
print("Espresso: $" + str(P_espresso))
print("Mocha: $" + str(P_mocha))

choice=input("Hello " + C_name + " What would you like to order? ")

if choice.lower() == "coffee":
    cost=P_coffee
elif choice.lower() == "latte":
    cost=P_latte
elif choice.lower() == "espresso":
    print("Sorry we donot have that.")
elif choice.lower() == "mocha":
    cost=P_mocha
else:
    print("I'm sorry, We donot have that.")

quantity=int(input("How many cups would you like? "))
T_cost=cost*quantity

stu=input("Are you a student? yes/no  ")
if stu.lower()=="yes":
    T_cost=T_cost-T_cost*0.1
elif quantity>1:
    print("You get a $1 discount.")
    T_cost-=1

print("Your total is: $" +str(T_cost))
print ("Thank you!, " +C_name+ " Please visit again.")


