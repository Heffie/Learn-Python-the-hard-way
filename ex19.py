# function that prints the amounts of cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man thats's enough for a party!")
    print("Get a blanket, \n")

# the function cheese_and_crackers strict values
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

# the function cheese_and_crackers with variables
print("Or, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# the function cheese_and_crackers with math
print("We can even do math inside it too:")
cheese_and_crackers(10 + 20, 4 + 6)

# the function cheese_and_crackers with variables and math
print("And we can combine the two, variables with math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
