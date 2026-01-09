num_symbols = int(input("Enter the number of symbols: "))

def draw_rhombus(num):
    all_symbols = num_symbols * 2
    rhombus_symbols = all_symbols - (2 * num)
    # recursive base
    if num == 0:
        return
    # pre-action
    print("*" * num," " * rhombus_symbols,"*" * num, sep="")
    # recursion with no return statement
    draw_rhombus(num - 1)
    # post-action
    print("#" * num, " " * rhombus_symbols, "#" * num, sep="")


draw_rhombus(num_symbols)