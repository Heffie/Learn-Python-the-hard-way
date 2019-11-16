i = 0
numbers = []

def while_loop(number,steps):
    i = 0
    numbers = []

    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + steps
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

def for_loop(start,stop,steps):
    i = 0
    numbers = []

    for i in range(start,stop,steps):
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + steps
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

while_loop(10,2)
for_loop(0,10,2)
