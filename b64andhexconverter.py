#   Written by J2Defend https://www.github.com/J2Defend (MIT Licensed)
#   This program was written to complete challenge 1 of cryptopals.com
#   This program simply takes user input and either converts hex to base64
#   or does the opposite based on the users selection.

import base64

#   This function converts hex to base64
def hex_to_base64 (h):
    print('Converting from hex to base64...')
    # Convert hex string to bytes
    h_bytes = bytes.fromhex(h)
    # Convert bytes to base64
    # .b64encode method returns a base 64 encoded byte object
    # .decode method is used to convert from bytes to base64
    b64 = base64.b64encode(h_bytes).decode()
    print('Your base64 string is: ' + b64)

#   This function converts base64 to hex
def base64_to_hex (b):
    print('Converting from base64 to hex...')
    # Convert base64 to bytes
    b_bytes = base64.b64decode(b)
    # Convert bytes to hex
    h3x = b_bytes.hex()
    print('Your hex string is: ' + h3x)

#   This is the, you guessed it, main function
def main ():
    # Ask the user for desired function
    get_function = input('Would you like to convert hex to base64 (h64) or convert base64 to hex (64h)? \n')

    # Perform appropriate action based on user input
    if get_function == 'h64':
        h = input('Input hex string: ')
        hex_to_base64(h)
    elif get_function == '64h':
        b = input('Input base64 string: ')
        base64_to_hex(b)
    else:
        print('Incorrect input. Exiting.')
        exit

#   We have blast off
main()