# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#CATCH UP CHALLENGE

num_1 = int(input("Enter a number over 100: "))
num_2 = int(input("Enter a number under 10: "))

result = num_1//num_2
print("{0} goes in {1} {2} times".format(num_2,num_1,result))


# %%
#IS IT RAINING?

rain = input("Is it raining? ")

if rain == "yes":
    windy = input("Is it windy? ")
    if windy == "yes":
        print("it's too windy for an umbrella")
    else:
        print("take an umbrella")
else:
    print("Enjoy your day")
    


# %%
# ENTER A NUMBER LOOP

num_1 = int(input("enter a number: "))
num_2 = int(input("enter another number: "))
result = num_1+num_2

add_number = input("Do you want to add another number? [yes/no] ")

while add_number == "yes":
    num_3 = int(input("enter the number: "))
    result = result + num_3
    add_number = input("Do you want to add another number? [yes/no] ")
else:
    print("The total is " + str(result))


