def strings_again_again(string):
    if len(string) == 1:
        return string[-1]
    else:
        return string[0] + "*" + strings_again_again(string[1:])