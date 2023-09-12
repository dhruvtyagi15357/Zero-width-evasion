import binascii
import FileIO as fio
import base64
import conversions as con
'''The program probably wont work if zero width characters already are present in the cover document'''

def mainn():
    i = 'y'
    while i == 'y':
        print("1. Hide the secret file content\'s content in cover file")
        print("2. Extract the hidden secret contents from input file and store the secret in output file")
        op = input("Select an option:")
        if op == '1':
            input_file_cover = input("Enter the name of the cover file: ")
            cover = fio.read_message(input_file_cover)
            input_file_secret = input("Enter the name of the secret file: ")
            secret = fio.read_file(input_file_secret)
            hex_of_secret = binascii.hexlify(secret).decode()
            binary_of_secret = con.hex_to_bin(hex_of_secret)
            final_output = cover + con.hideString(binary_of_secret)
            output_file = input("Enter the name of the output file: ")
            fio.write_message(final_output, output_file)
            print("Operation successful!")

        elif op == '2':
            input_file_name = input("Enter the name of the file from which you want to extract the hidden string")
            entire_file_with_hidden_secret = fio.read_message(input_file_name)
            hidden_message_binary = con.find_hidden_message(entire_file_with_hidden_secret)
            hidden_message_hex = con.extract_hex(hidden_message_binary)
            hidden_message = binascii.unhexlify(hidden_message_hex).decode()
            output_file_name = input("Enter the name of the output file.")
            fio.write_message(hidden_message, output_file_name)
            
        else:
            print("wrong choice!")
        i = input("Run again?\n")[0].lower()


if __name__ == '__main__':
    mainn()
