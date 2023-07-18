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

def menu():
    print("Please select an option")
    print("1. Encode my password")
    print("2. Decode my password")
    print("3. Exit")
    return

if __name__ == "__main__":
    coding = True
    while coding == True:
        menu()
        choice = int(input())
        if choice == 1:
            print("Enter the password to decode:", end = '')
            new_password = encoder(str(input()))
            print(new_password)

        if choice == 2:
            '''place decoder function here'''

        if choice == 3:
            print("Dueces!")
            break
        if choice < 0 or choice > 3:
            print("That is not a valid option!")
