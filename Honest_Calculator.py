# write your code here
# messages
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_10, msg_11, msg_12]


def is_one_digit(v):
    v = float(v)
    if v.is_integer() and v in range(-10, 10):
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2) or v1 == v2:
        msg += msg_6
    if v1 == '1' or v2 == '1' and v3 == '*':
        msg += msg_7
    if v1 == '0' or v2 == '0' and v3 in ['+', '-', '*']:
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


memory = 0.0
while (True):

    calc = input(msg_0)
    calc = calc.split()
    operands = ["+", "-", "*", "/"]
    x = calc[0]
    operand = calc[1]
    y = calc[2]

    if calc[0] == 'M':
        x = memory
    if calc[2] == 'M':
        y = memory

    try:
        (float(x) and float(y))
    except:
        print(msg_1)
        continue
    else:
        if operand in operands:
            check(x, y, operand)
            x = float(x)
            y = float(y)
            if operand == '+':
                result = x + y
            if operand == '-':
                result = x - y
            if operand == '*':
                result = x * y
            if operand == '/':
                if y != 0:
                    result = x / y
                else:
                    print("Yeah... division by zero. Smart move...")
                    continue

            print(result)
            answer = input(msg_4)

            if answer == 'y':
                if is_one_digit(result):
                    msg_index = 0
                    while (msg_index <= 2):
                        if answer == 'n':
                            break
                        answer = input(msg_[msg_index])
                        msg_index += 1
                else:
                    memory = result
            answer = input(msg_5)
            if answer == 'y':
                continue
            if answer == 'n':
                break

        else:
            print(msg_2)
            continue


def main():
    pass


if __name__ == "__main__" :
    main()