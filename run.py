# RPG-7 Random Password Generator
import string
# Faker is a handy wee module that generates fake data like real-sounding words
# and sentences for a variety of purposes; we're only interested in the method
# 'word()' which returns a random English word for use in generate_passphrase()
# https://faker.readthedocs.io/en/master/
from faker import Faker
import secrets
import math
import random
# PyDrive is a very helpful wrapper library of google-api-python-client which
# manages Google Drive operations, such as authenticating with Google Drive
# and creating files
# https://pypi.org/project/PyDrive/
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def get_user_input():
    """
    Get five comma-separated characters from user for password options.
    Run while loop to repeat request for input until user input is valid;
    input must be five comma-separated characters e.g. 18,Y,Y,5,N
    """

    # Give instructions to user on how to use RPG-7
    print('Please enter the features you would like your password(s) to have:')
    print('1. Number of characters (a number between 8 and 25)')
    print('2. Include special characters? (e.g. £, $, *, /, ;, etc.) (Y/N)')
    print('3. Passphrase-like? (password(s) will consist of few words) (Y/N)')
    print('4. Number of passwords (a number between 1 and 10)')
    print('5. Save to Google Drive? (File can then be saved locally) (Y/N)')
    print()
    print('For example, if you want three 12-character passwords with special')
    print('characters not consisting of words and not have them saved to a ')
    print('file in Google Drive, you would enter 12,Y,N,3,N')
    print()
    print('This would give an example output of: ')
    print('0x0I2£KDQx8/')
    print('6U4x0"d$>>"4')
    print('Xn72*1{!:=b^')
    print()

    # Improve readability of loop with named variable indicating
    # validity of user input
    valid = False

    while not valid:
        user_input = input('Please enter your password options here: \n')

        # Split user input into list of strings in preparation
        # for data validation
        password_options = user_input.split(",")

        # Set valid to True if password options are valid to
        # end loop (improves readability a bit)
        valid = validate_user_input(password_options)

    return password_options


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
            raise ValueError(f"5 options required; {len(user_input)} entered")

        # Unpack options into five variables
        first, second, third, fourth, fifth = user_input

        # Check if second, third and and fifth options are
        # 'Y' or 'N' as expected (this was more readable at
        # first but I had to change the line lengths to
        # conform to pep8 Python validation)
        s_up = second.upper() not in YES_NO_OPTIONS
        t_up = third.upper() not in YES_NO_OPTIONS
        f_up = fifth.upper() not in YES_NO_OPTIONS
        if s_up or t_up or f_up:
            # Again, this was initially more informative but needs to conform
            # to pep8 Python validation
            # Initally had '; \nyou entered {second} (2nd),
            # {third} (3rd), {fifth} (5th)' at the end, which is obviously
            # more informative
            raise ValueError("The 2nd, 3rd and 5th options must be Y or N")

        # ValueError exception will be raised if either first or
        # fourth (or both) can't be converted to integers
        first_int = int(first)
        fourth_int = int(fourth)

        # Check if first option is between 8 and 25 and
        # fourth option is between 1 and 10 as expected
        firstInRange = first_int not in [num for num in range(8, 26)]
        fourthInRange = fourth_int not in [num for num in range(1, 11)]
        if firstInRange or fourthInRange:
            # Again, this was initially more informative but needs to conform
            # to pep8 Python validation
            # Initially had "The first option must be between 8 and 25 and the
            # fourth option must be \nbetween 1 and 10; you entered
            # {first_int} (first), {fourth_int} (fourth)"
            raise ValueError("First and/or fourth options out of range")

    except ValueError as e:
        print()
        print("**************************************************************")
        print(f"Error with input: \n{e}. Please try again.")
        print("**************************************************************")
        print()
        return False

    return True


def generate_password(num_chars, special, phrase):
    """
    Generate and return random password as per user's specification
    """

    password = []

    # If passphrase chosen, call generate_passphrase()
    if phrase:
        password = generate_passphrase(num_chars, special)

    if not password:
        # Generate password consisting of random characters

        # All lowercase and uppercase alphanumeric characters in English
        # language (including two sets of all digits so more numbers
        # appear in password)
        ALPHA_NUM = string.ascii_letters + (string.digits*2)

        # secrets.choice(ALPHA_NUM) returns random element of ALPHA_NUM;
        # secrets is also better than other modules as it is more secure
        # and cryptographically stronger
        # (https://docs.python.org/3/library/secrets.html)
        password = [secrets.choice(ALPHA_NUM) for i in range(0, num_chars)]

        if special:
            password = insert_special_chars(password, phrase)

    # Convert to string
    password_string = ''.join(str(char) for char in password)

    return password_string


def generate_passphrase(num_chars, special):
    """
    Generate and return a collection of random words (a phrase)
    with various letters replaced by numbers
    """

    passphrase = []
    fake = Faker()

    while len(passphrase) < num_chars:
        word = fake.word()
        letter_to_num = {'a': '4', 'e': '3', 'i': '1',
                         'o': '0', 's': '5', 'z': '2'}

        # This checks that the word is less than seven characters, as words
        # that are too long are less memorable and readable, and that the
        # length of the final passphrase won't exceed num_chars (the password
        # length specified by the user at the start of the program)
        if len(word) <= 7 and len(word) < (num_chars - len(passphrase)):
            word = word.capitalize()

            # This loop is necessary as passphrase needs to be a list of
            # characters for now, not a list of words.
            # It also substitutes out certain letters for numbers
            for letter in word:
                if letter in letter_to_num.keys():
                    letter = letter_to_num[letter]
                passphrase.append(letter)

            if special:
                passphrase = insert_special_chars(passphrase, True)

        # If there are only one or two characters left until the specified
        # password length then just append 2 special characters if specified,
        # else append random 1-letter or 2-letter word (with numbers inserted)
        chars_left = num_chars - len(passphrase)
        if 0 < chars_left < 3:
            if special:
                passphrase = insert_special_chars(passphrase, True)
            else:
                if chars_left == 1:
                    # '4' instead of 'a', '1' instead of 'i'
                    passphrase.append(secrets.choice(['4', '1']))
                else:
                    two_letter_words = ['4t', 'my', '4n', 'h3', 'b3', 't0']
                    for letter in secrets.choice(two_letter_words):
                        passphrase.append(letter)

    return passphrase


def insert_special_chars(password, phrase):
    """
    Insert special characters into password list at random places.
    If 'phrase' is True, append and prepend special characters.
    """

    SPECIAL = string.punctuation

    # The reason we use math.floor(len(password)/4) is because we only want
    # relatively few special characters as they
    # are a bit harder to remember in a password
    num_special = math.floor(len(password)/4)

    # If dealing with passphrase, just append a special character as we will
    # be calling insert_special_chars() after every word in the phrase, ending
    # up with something like S0M3£Gr33n$Tr33s*, instead of S£0M3G$r33nTr*33s,
    # thus maintaining the readability inherent in a passphrase
    if phrase:
        password.append(secrets.choice(SPECIAL))
        return password

    chosen_sp_chars = [secrets.choice(SPECIAL) for i in range(0, num_special)]

    # Replace random characters with randomly chosen special characters and
    # shuffle password
    for char in chosen_sp_chars:
        password[secrets.randbelow(len(password))] = char

    random.shuffle(password)

    return password


def save_to_gdrive(password):
    """
    Save password to file in Google Drive using user-supplied file name.
    """
    # Authenticate using GoogleAuth() method of PyDrive and use to set up
    # instance of Google Drive
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    # Again, this was originally more informative but had to change
    # to conform to pep3 Python validation;
    # initially had "What would you like the name of the file to be?"
    file_name = input("Name of Google Drive file? (e.g. MyPasswords): \n")
    file_name = file_name + ".txt"

    # Create and write to file in Google Drive using user-supplied file name
    file = drive.CreateFile({'title': file_name})
    file.SetContentString(password)
    file.Upload()

    print(f'Password written to {file_name} in Google Drive!')


def main():
    """
    Run program
    """
    print('Welcome to RPG-7 (Random Password Generator)!')
    print()
    user_input = get_user_input()
    print()

    # Unpack validated user_input to provide variables
    # with which to configure password
    num_chars, sp_chars, passphrase, num_passwords, write_to_gdoc = user_input
    num_chars = int(num_chars)
    num_passwords = int(num_passwords)

    # Convert special_chars, passphrase and write_to_gdoc to boolean values
    sp_chars = True if (sp_chars.upper() == 'Y') else False
    passphrase = True if (passphrase.upper() == 'Y') else False
    write_to_gdoc = True if (write_to_gdoc.upper() == 'Y') else False

    # Loop to implement number of passwords (fourth option) functionality
    password = ''
    for _ in range(num_passwords):
        password += generate_password(num_chars, sp_chars, passphrase) + '\n'

    if not write_to_gdoc:
        # password[:-1] is used to leave out last \n
        print(password[:-1])
    else:
        save_to_gdrive(password)


main()
