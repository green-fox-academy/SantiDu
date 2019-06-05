def strings_again(string):
    if len(string) == 0:
        return ""
    if string[0] == "x":
        return strings_again(string[1:])
    else:
        return string[0] + strings_again(string[1:])