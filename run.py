def get_user_input():
    """
    Get five comma-separated characters from user for password options.
    Run while loop to repeat request for input until user input is valid;
    input must be five comma-separated characters e.g. 18,Y,Y,5,N
    """

    # Give instructions to user on how to use RPG-7
    print('Please enter the features you would like your random password(s) to have:')
    print('1. Number of characters (a number between 8 and 25)')
    print('2. Include special characters? (e.g. £, $, *, /, ;, etc.) (Y/N)')
    print('3. Passphrase-like? (password(s) will consist of a few words) (Y/N)')
    print('4. Number of passwords (a number between 1 and 10)')
    print('5. Save to a Google Docs document? (File can then be saved locally) (Y/N)')
    print()
    print('For example, if you want three 12-character passwords with special ')
    print('characters not consisting of words and not have them saved to a ')
    print('file in Google Drive, you would enter 12,Y,N,3,N')
    print()
    print('This would give an example output of: ')
    print('0x0I2£KDQx8/')
    print('6U4x0"d$>>"4')
    print('Xn72*1{!:=b^')
    print()

    # Improve readability of loop with named variable indicating validity of user input
    valid = False

    while not valid:
        user_input = input('Please enter your password options here: ')

        # Split user input into list of strings in preparation for data validation
        password_options = user_input.split(",")

        # Set valid to True if password options are valid to end loop (improves readability a bit)
        valid = validate_user_input(password_options)

    return password_options


    #print(f"In get_user_input() function and here is user input: {user_input}")


def validate_user_input(user_input):
    """
    Ensures five values present, that the first and fourth values are 
    integers and that the second, third and fifth values are one of 
    'Y' or 'N'.
    Raises ValueError if any of this isn't the case.
    """

    YES_NO_OPTIONS = ['Y', 'N']

    try:
        if len(user_input) != 5:
            raise ValueError(f"5 options are required to create your random password(s); you entered {len(user_input)}")
        
    except ValueError as e:
        print()
        print("****************************************************************************")
        print(f"Error with input: {e}. Please try again")
        print("****************************************************************************")
        print()
        return False
    
    return True


def main():
    """
    Run program
    """
    print('Welcome to RPG-7 (Random Password Generator)!')
    print()
    user_input = get_user_input()
    print()

main()