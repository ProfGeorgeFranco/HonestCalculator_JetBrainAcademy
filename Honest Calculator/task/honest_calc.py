msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_order = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

operand = ['+', '-', '*', '/']

calc_list = []

x = 0.0

y = 0.0

memory = 0.0

result = 0.0

op = ""

done_calc = False

check_ok = False

calculator_ok = False

memory_ok = False


def begin():
    global calc_list, check_ok

    print(msg_0)

    calc_list = input().split()

    check_ok = False


def check_data():
    global calc_list, x, y, op, operand, done_calc, check_ok

    while not check_ok:
        try:
            x = calc_list[0]
            op = calc_list[1]
            y = calc_list[2]
        except IndexError:
            print(f"Not enough parameters in equation => Missing {3 - len(calc_list)}")
            done_calc = False
            check_ok = False
            break

        if x == "M":
            x = float(memory)
        else:
            try:
                x = float(calc_list[0])
            except ValueError:
                print(msg_1)
                check_ok = False
                break

        if y == "M":
            y = float(memory)
        else:
            try:
                y = float(calc_list[2])
            except ValueError:
                print(msg_1)
                check_ok = False
                break

        if op not in operand:
            check_ok = False
            print(msg_2)
            break

        check_ok = True


def calculator():
    global x, y, op, check_ok, result, calculator_ok

    calculator_ok = False

    if op == "+":
        result = x + y
        print(result)
        calculator_ok = True

    elif op == "-":
        result = x - y
        print(result)
        calculator_ok = True

    elif op == "*":
        result = x * y
        print(result)
        calculator_ok = True

    elif op == "/":
        if y != 0:
            result = x / y
            print(result)
            calculator_ok = True

        elif y == 0:
            print(msg_3)
            check_ok = False
            calculator_ok = False


def memory_option():
    global memory, result, memory_ok

    msg_index = 0
    while True:
        print(msg_4)
        user_choice1 = input()
        if user_choice1 == "y":

            if is_one_digit(result):
                msg_index = 10

                while True:
                    print(msg_order[msg_index])

                    user_choice2 = input()

                    if user_choice2 == "y":
                        if msg_index < 12:
                            msg_index += 1

                        else:
                            memory = result
                            return

                    if user_choice2 == 'n':
                        return

            else:
                memory = result
                return

        elif user_choice1 == "n":
            return


def user_continue():

    while True:
        print(msg_5)
        user_choice = input()
        if user_choice == "y":
            return False
        elif user_choice == "n":
            return True


def is_one_digit(n):

    if -10 < n < 10 and n.is_integer():
        output = True

    else:
        output = False

    return output


def check_lazy(x0, y2, op1):
    msg = ""

    if is_one_digit(x0) and is_one_digit(y2):
        msg += msg_6

    if (x0 == 1 or y2 == 1) and op1 == "*":
        msg += msg_7

    if (x0 == 0 or y2 == 0) and (op1 in ['+', '-', '*']):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


while not done_calc:
    begin()

    if not check_ok:
        check_data()

    if check_ok:
        check_lazy(x, y, op)
        calculator()

    if calculator_ok:
        memory_option()
        done_calc = user_continue()
