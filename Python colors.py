## FOR PYTHON IF YOU WANT TO USE RGB COLORS IN THE TERMINAL ##
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


print(colored(255, 0, 0, "HELLO WORLD"))
# WHERE THE FIRST VALUE IS R, SECOND IS G, THIRD IS B, AND THE LAST IS THE TEXT YOU WANT TO PRINT
