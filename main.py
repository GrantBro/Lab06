def main():
    return


def encoder(code):
    num_code = []
    for i, v in enumerate(code):
        num_code.append(int(v))
    for i in range(len(num_code)):
        num_code[i] += 3
        num_code[i] = str(num_code[i])
    encoded_pass = ''.join(num_code)
    return encoded_pass


# hello edit!! hey grant, make sure to comment on code :)


def decode_password(encoded_password):
    decoded_password = ""  # initialize empty string
    for digit in encoded_password:  # iterate over each digit with for loop
        # Convert the digit to an integer, subtract 3, and wrap around if it goes below 0
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


def menu():
    print("Please select an option")
    print("1. Encode my password")
    print("2. Decode my password")
    print("3. Exit")
    return


if __name__ == "__main__":
    coding = True
    while True:
        menu()
        choice = int(input())
        if choice == 1:
            print("Enter the password to encode:", end='')
            new_password = encoder(str(input()))
            print(new_password)

        elif choice == 2:  # inverse of 1, intakes 8 dig, converts to original password.
            encoded_password = input("Enter the password to encode: ")
            if len(encoded_password) == 8:
                decoded_password = decode_password(encoded_password)
                print("Decoded password:", decoded_password)
            else:  # if not 8 dig, print error
                print("Invalid encoded password. Please enter an 8-digit encoded password.")

        elif choice == 3:
            print("Deuces!")
            break
        elif choice < 0 or choice > 3:
            print("That is not a valid option!")
