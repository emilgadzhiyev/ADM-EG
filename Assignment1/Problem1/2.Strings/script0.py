# sWAP cASE

def swap_case(s):
    x = ""
    for let in s:
        if let.isupper() == True:
            x += (let.lower())
        else:
            x += (let.upper())
    return x
