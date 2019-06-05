def rec_strings(string):
    if len(string) == 0:
        return ""
    if string[0] == "x":
        return "y" + rec_strings(string[1:])
    else:
        return string[0] + rec_strings(string[1:])