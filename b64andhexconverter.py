import base64

def hex_to_base64 (h):
    print('Converting from hex to base64...')
    h_bytes = bytes.fromhex(h)
    b64 = base64.b64encode(h_bytes).decode()
    print('Your base64 string is: ' + b64)

def base64_to_hex (b):
    print('Converting from base64 to hex...')
    b_bytes = base64.b64decode(b)
    h3x = b_bytes.hex()
    print('Your hex string is: ' + h3x)

def main ():
    get_function = input('Would you like to convert hex to base64 (h64) or convert base64 to hex (64h)? \n')

    if get_function == 'h64':
        h = input('Input hex string: ')
        hex_to_base64(h)
    elif get_function == '64h':
        b = input('Input base64 string: ')
        base64_to_hex(b)
    else:
        print('Incorrect input. Exiting.')
        exit

main()