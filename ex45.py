# Game hef-it office
# Rooms
    # 1. Enterance
    # 2. Developers room -> Giant bug to destroy!
    # 3. Support room -> The never ending end user!
    # 4. Automation room -> The AI that is automating your work!
# Rewards per room
# Register

from sys import exit
import smtplib

def start():
    print("Welcome to hef-it digital office!")
    print("You are entering the office and our assistance Sara is glad to help you. ")
    print("Say 'Hi to Sara'")

    choice = input("> ")

    if choice == "hi Sara" or choice == "hi":
        print("Sara: Hi.... uhh what is your name?")
        registration()
    else:
        print("Sorry, i cant help you with that. You can say 'Sara Help'.")

def registration():
    print("Can i get your name?")

    name = input("> ")

    if name != "":
        print(f"Ok, i'll will note '{name}'.")
        rooms()
    else:
        print("Sorry come again?")
        start.name = input("> ")
        registration()

def rooms():
    print("Do you want to go to de 'developers room', 'support room' or 'automation room'?")
    choice = input("> ")

    if choice == "developers room":
        developers_room()
    elif choice == "support rooms":
        support_room()
    elif choice == "automation room":
        automation_room()
    else:
        print("Thats no option")
        rooms()

def developers_room():
    print("You enter the developers room.")
    print("You see a giant bug standing in the room messing up all code!")
    print("""What do you do?
            a: Spray the bug?
            b: Delete all code?
            c: Run!
    """)
    choice = input("> ")

    if choice == "a":
        print("The bug eats your head! And go on bugging..")
    elif choice == "b":
        print("All code deleted, but the bug is gone.")
        finish()
    elif choice == "c":
        print("You trip, you die.")
    else:
        print("To bad you're gone")

def support_room():
    print("You enter the support room.")
    print("YOu see an end user sitting there...")
    print("""What do you do?
            a: Ask if yo can help?
            b: Beat him with a bat!
            c: Tell him that every computer problem sits between the desk and chair?
    """)
    choice = input("> ")

    if choice == "a":
        print("Good choice!")
        finish()
    elif choice == "b":
        print("The end user is gone but the problem still present")
    elif choice == "c":
        print("You get beat with a bat!")
    else:
        print("To bad you're gone")

def automation_room():
    print("You enter the automation room.")
    print("You see a giant robot automating all your work")
    print("""What do you do?
            a: Throw some water?
            b: See 'beep-bob-beep'?
            c: Say terminator is your brother in law?
    """)
    choice = input("> ")

    if choice == "a":
        print("Good choice!")
        print("__Finish")
    elif choice == "b":
        print("The end user is gone but the problem still present")
    elif choice == "c":
        print("You get beat with a bat!")
    else:
        print("To bad you're gone")


def finish():
    print("You are a super hero!")
    print(f"We @ hef-it would gladly get to know you! {name}")
    print("Please fill in the information so we can contact you :)")

    email = input("e-mail? >")
    phone = input("Telefoon nummer? >")

    print("Have a nice day hero!")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("jeffrey@hef-it.nl" , "PASSWORD")

    msg = "Finisher hef-it game"
    server.sendmail("jeffrey@hef-it.nl", "jeffrey@hef-it.nl", msg)
    server.quit()


start()
