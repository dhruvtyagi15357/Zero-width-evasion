def read_message(filename):  # name of file as a string
    file1 = open(filename, 'r', encoding="utf-8")
    message = file1.read()
    file1.close()
    return message

def write_message(message, fname):
    with open(fname, 'w', encoding="utf-8") as file:
        file.write(message, )

def read_file(path):
    with open(path, 'rb') as file:
        msg = file.read()
    return msg