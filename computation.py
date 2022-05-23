first = 0
symbol = ''
second = 0

# Starting state (States are:  first -> symbol -> second -> output )
state = "first"
check = ''



def user_input():
    check = input("Input = ")
    print("IN USER_INPUT: CHECK =") # TEST PRINT
    print(check) # TEST PRINT
    print("") # TEST PRINT
    return check


def clear_input():
    pass

def handle_first(check, state):
    #Check repetitive
    if state == "first":
        first = check
        state = "symbol"

        print("IN HANDLE_FIRST: FIRST - STATE") # TEST PRINT
        print(f"{first}{state}") # TEST PRINT

        return first, state



def handle_operator():
    pass
    ## Using old code as a "template, but will simplify it later"
# if symbol == "+":
#     output = first + second

# if symbol == "-":
#     output = first - second

# if symbol == "x":
#     output = first * second

# if symbol == "/":
#     output = first / second

# print("")
# print("")
# print(f"Answer:")
# print(f"{first} {symbol} {second} = {output}")
# print("")


def handle_second():
    pass

def output_answer():
    pass


def check_input(check, state):
    if state == "first":
        try:
            check = int(check)
            return check
        except ValueError:
            print("Not an integer")         

    if state == "symbol":
        allowed_symbols = ["+", "-", "x", "/", "add", "sub", "mul", "div"]
        if check in allowed_symbols:
            return check
        print("Not a valid symbol!  +, -, x, / ")

    if state == "second":
        try:
            check = int(check)
            return check
        except ValueError:
            print("Not an integer")







run = True

while run:


    print("")
    print("============")
    print(f"First = {first}")
    print(f"Symbol = {symbol}")
    print(f"Second = {second}")
    print(f"State = {state}")
    print(f"Check = {check}")
    print("============")
    print("")


    user_input()
    print("After input") # TEST PRINT
    
    check_input(check, state)
    print("After check") # TEST PRINT

    if state == "first":
        handle_first(check, state) #State input is repetitive
        print("After handle_first") # TEST PRINT

    if state == "symbol":
        handle_operator()
    











## Notes
# while run -> Get user input
#   if state = first -> handle first
#                           is number? else: print(Not digit)
#                           if at least 1 number: receive number or operator
#   elif state = second -> handle second
#   else -> compute result

# Files
# main, calc, validate

# Pygame uses events rather than states
# (Moreso get event)
