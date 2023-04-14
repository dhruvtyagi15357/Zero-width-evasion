def mapp(char):
    char = str(char)
    if char.lower() == 'a':
        return 10
    elif char.lower() == 'b':
        return 11
    elif char.lower() == 'c':
        return 12
    elif char.lower() == 'd':
        return 13
    elif char.lower() == 'e':
        return 14
    elif char.lower() == 'f':
        return 15
    else:
        return char

def hex_to_bin(l):
    result = ""
    for i in l:
        tba = bin(int(mapp(i)))[2:]
        if len(tba) != 4:
            tba = ("0"*(4-len(tba))) + tba
        result += tba 
    return result


def switchBintohex(arg):
    switcher = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": 'A',
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }
    return switcher.get(arg)

def extract_hex(binn):
    quads = []
    quad = ""
    for i in range(0, len(binn)):
        if len(quad) != 4:
            quad += binn[i]
        else:
            quads.append(quad)
            quad = binn[i]

    quads.append(quad)
    hex = ""
    for j in quads:
        hex += switchBintohex(j)
    return hex

def hideString(binn):
    zero = u'\u200b'
    one = u'\u200c'
    result = ""
    for i in binn:
        if i == '0':
            result += zero
        else:
            result += one
    return result

def find_hidden_message(s):
    sec_bin = ""
    for i in range(0, len(s)):
        if s[i] == u'\u200b':
            sec_bin += '0'
        elif s[i] == u'\u200c':
            sec_bin += '1'
    return sec_bin