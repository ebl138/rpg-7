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