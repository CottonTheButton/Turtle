#!/usr/local/bin/python3.8
import sys, os
import turtle


try:
    first_arg = sys.argv[1]


    if first_arg == "corona":
        print(turtle.corona())

        
    elif first_arg == "factorial":

        try:

            numz = sys.argv[2]
            num = int(numz)

            x = 0
            y = num

            while x < num:
                if y != 1:
                    print(f"{y} * ", end="")
                else:
                    print(y)
                x += 1
                y -= 1

            turtle.factorial(num)

        except IndexError:
            print("Syntax: turtles factorial <number that you want to get that factorial of>")
    
    elif first_arg == "help":
        commands_list = []

    elif first_arg == "solve":

        operator = sys.argv[2]
        turtle.solve(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

    elif first_arg == "talk":
        print("WIP")
        
    else:
        print("What do you want me to do? >__<")

except IndexError:
    print("What do you want me to do? >__<")