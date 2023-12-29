def get_user_input():
    """
    Get five comma-separated characters from user for password options.
    Run while loop to repeat request for input until user input is valid;
    input must be five comma-separated characters e.g. 18,Y,Y,5,N
    """

    user_input = input('Please enter your password options here: ')

    print(f"In get_user_input() function and here is user input: {user_input}")

def main():
    """
    Run program
    """
    print('Welcome to RPG-7 (Random Password Generator)!')
    print()
    user_input = get_user_input()
    print()

main()