def main():
    return


def encoder(code):  # intake str password
    num_code = []
    for i, v in enumerate(code):  # use values of string to change
        num_code.append(int(v))
    for i in range(len(num_code)):
        num_code[i] += 3  # chang values by +3
        if num_code[i] >= 10:  # Use ones digit for values higher than 10 after +3
            num_code[i] = num_code[i] % 10
        num_code[i] = str(num_code[i])
    encoded_pass = ''.join(num_code)  # turn new digits in string form in list to a complete string.
    return encoded_pass
# hello edit!! hey grant, make sure to comment on code :)


def decode_password(encoded_password):
    decoded_password = ""  # initialize empty string
    for digit in encoded_password:  # iterate over each digit with for loop
        # Convert the digit to an integer, subtract 3, and wrap around if it goes below 0
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


def menu():  # simple repeatable menu
    print("Please select an option")
    print("1. Encode my password")
    print("2. Decode my password")
    print("3. Exit")
    print("Select an option to perform.")
    return


if __name__ == "__main__":
    coding = True  # main loop
    while True:
        menu()
        choice = int(input())  # choice option by user
        if choice == 1:
            print("Enter an 8-Digit password to encode:", end='')
            new_password = input()
            try:  # checking to see if letters exist within the input
                new_password = int(new_password)
            except ValueError:
                print('The 8-digit password contains an incorrect character. Please try again')
            if len(str(new_password)) != 8:  # must be string of 8 digits, no more, no less
                print('That is an an valid password! Please type and 8-Digit password')
            elif len(str(new_password)) == 8:
                # correct ValueType and length of password for encoder function to properly operate
                new_password = encoder(str(new_password))
                print(f'The encoded password is: {new_password}')
        elif choice == 2:  # inverse of 1, intakes 8 dig, converts to original password.
            encoded_password = input("Enter the password to encode: ")
            if len(encoded_password) == 8:
                decoded_password = decode_password(encoded_password)
                print("Decoded password:", decoded_password)
            else:  # if not 8 dig, print error
                print("Invalid encoded password. Please enter an 8-digit encoded password.")

        elif choice == 3:  # leaving the loop and exiting the program
            print("Deuces!")
            break
        elif choice < 0 or choice > 3:  # making ure user input is within menu options
            print("That is not a valid option!")
