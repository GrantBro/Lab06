def main():
    return


def encoder(code):
    num_code = []
    for i, v in enumerate(code):
        num_code.append(int(v))
    for i in range(len(num_code)):
        num_code[i] += 3
        if num_code[i] >= 10:
            num_code[i] = num_code[i] % 10
        num_code[i] = str(num_code[i])
    encoded_pass = ''.join(num_code)
    return encoded_pass

def menu():
    print("Please select an option")
    print("1. Encode my password")
    print("2. Decode my password")
    print("3. Exit")
    print("Select an option to perform.")
    return

if __name__ == "__main__":
    coding = True
    while coding == True:
        menu()
        choice = int(input())
        if choice == 1:
            print("Enter an 8-Digit password to encode:", end = '')
            try:
               new_password = int(input())
            except ValueError:
                print('The 8-digit password contains an incorrect character. Please try again')
            if len(str(new_password)) != 8:
                print('That is an an valid password! Please type and 8-Digit password')
            elif len(str(new_password)) == 8:
                new_password = encoder(str(new_password))
                print(f'The encoded password is: {new_password}')


        if choice == 2:
            '''place decoder function here'''

        if choice == 3:
            print("Dueces!")
            break
        if choice < 0 or choice > 3:
            print("That is not a valid option!")
