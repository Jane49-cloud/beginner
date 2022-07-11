

# if conditional statements

# first instance
is_hot = False
is_cold = True
if is_hot:
    print("Its a hot day!")
    print("Drink alot of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("enjoy your day!")
# second instance

price = 1000000
good_credit = True
if good_credit:
    down_pay = 10/100
    result = price * down_pay
else:
    down_pay = 20 / 100
    result = price * down_pay
print(f"Down payment:${result}")

# comparison operators
age = 50
if age > 20:
    print("You are responsible for your life")
else:
    print("You are still under your parents care!")


# another condition statement
weight = int(input("please enter your weight..."))
value = input("is it in pounds or kilograms?")
if value.upper() == "pounds" :
    print(f"your  weight is {weight / 0.45} kilograms")
elif value.upper() == "kilograms":
    print(f"your weight {weight*0.45} ")


