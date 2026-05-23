print("Hello welcome to my coffee shop!!")

name = input("What is your name?\n")

if name == "Bill" or name == "William" or name == "Patrick" or name == "Diego" or name == "Helene" or name == "Julia":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deeds < 4:
        print("You're not welcome here evil " + name + ", get outta here!!")
        exit()
    else:
        print("Nice to meet you "+ name + " thank you for coming in today!!\n\n")

menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"

print("So " + name + ", what would you like to order today? "+ menu)

order = input()

if order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 4
elif order == "Latte":
    price = 6
elif order == "Cappuccino":
    price = 8
elif order == "Frappuccino":
    price = 9
else:
    print("Well if you don't want coffee why are you even here?")
    exit()

quantity = input("How many " + order + " would you like today?\n")

total = price * int(quantity)

print("that will cost: $" + str(total))

if input("Is that alright?\n") == "yes":
    print("Thank you " + name + ", we will have your " + quantity + ' ' + order + " ready in a bit!!")
else:
    print("Get out of here you bum!!")

    