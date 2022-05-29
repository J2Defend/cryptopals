#   Written by J2Defend https://www.github.com/J2Defend (MIT Licensed)
#   This program was written to complete challenge 2 of cryptopals.com
#   This program simply takes a user hex string and hex key string
#   and computes the XOR of the two strings.

#   This function gets the user string (hex) to be XOR'd
def get_input ():
    h3x = input('Input hex string: \n')
    # Convert hex to bytearray
    h3x_bytes = bytearray.fromhex(h3x)
    return h3x_bytes

#   This function gets the user key string (hex)
def get_key ():
    key = input('Input XOR hex key: \n')
    # Convert hex to bytearray
    key_bytes = bytearray.fromhex(key)
    return key_bytes

#   This function performs the XOR
def xor_function (inputText, key):
    # Create an empty bytearray the length of the input string
    output = bytearray(len(inputText))
    # Perform XOR
    for i in range(len(inputText)):
        output[i] = inputText[i] ^ key[i]
    # Convert bytearray to bytes
    output_bytes = bytes(output)
    print(output_bytes.hex())

#   This is the, you guessed it, main function
def main ():
    xor_function(get_input(), get_key())

#   We have blast off
main()