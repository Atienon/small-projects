'''
This is a Python script to convert a binary number to a decimal number.
To start, the user can enter up to 8 binary digits in one input field.
Another version of this script lets the user enter a variable number of binary digits.
The program will validate the binary number (0s & 1s only) and then return the decimal number
without using a list.
'''

def bin2dec(binary_number):

    # Checking the length of the input, in the case the user can only input up to 8 binary digits
    #if len(binary_number) > 8:
    #    return "Please enter up to 8 binary digits"

    # Checking the validity of the number
    for char in binary_number:
        if char not in ["0", "1"]:
            return "Please enter a binary number (0s & 1s)"

    # Preparing answer
    answer = 0
    for i in range(len(binary_number)):
        answer += int(binary_number[(len(binary_number) - 1) - i]) * 2 ** i

    return answer

# Test

while True:

    user_input = input("Enter a binary number: 'q' to quit ")

    if user_input == 'q':
        break

    print(bin2dec(user_input))
