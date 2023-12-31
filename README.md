# RPG-7 Random Password Generator

RPG-7 is a Python terminal applicaton, which runs in the Code Institute mock terminal on Heroku.

Users can generate random password(s) as per their desired specification and receive these either as direct output 
from the terminal or have them saved to a document in Google Drive.

[Live version of the project](https://rpg-7-05e54012230e.herokuapp.com/)

![Am I Responsive mockup](https://raw.githubusercontent.com/ebl138/rpg-7/main/media/RPG-7-responsive-mockup.png)

## How to use

Users will be presented with instructions on using the application in Heroku.

Five comma-separated values are entered at the indicated point in the following format: 15,Y,N,6,Y

Each value indicates a feature that a user does/doesn't want to include and allows the user to make the password 
stronger/weaker as they desire.

There are five options for users to specify depending on how strong and random they want their password(s) to be:

1. The length of their password(s): this is the length, in characters, the user's password(s) will be e.g. 10 would 
generate password(s) consisting of 10 characters; must be a number between 8 and 25
2. Inclusion of special characters: the user can specify whether they want special characters in their password with 
Y for yes or N for no
3. Passphrase structure: the user can specify whether they want the password to consist of words, which are obviously 
more memorable, rather than random characters with Y for yes or N for no
4. Total number of passwords: this is the total number of passwords which will be generated; must be a number between 
1 and 10
5. Save in Google Drive file: this allows the user to save their password(s) in a file in Google Drive with Y for yes 
or N for no; N will print the password(s) to the terminal

The instructions are presented to the user as follows:

![User instructions](https://raw.githubusercontent.com/ebl138/rpg-7/main/media/user-instructions.png)

## Features

### Existing features

- __Random, strong password generation__

  - Passwords are created by randomly choosing alphanumeric characters (including both uppercase and lowercase letters) 
    using the secure, cryptographically strong Python module 'Secrets', which is more random than the 'random' module.
  - Passwords are output as text, either in the terminal or to a file in Google Drive, which allows for easy copy/pasting.
  - Example of strongest password generated:

![First feature](https://raw.githubusercontent.com/ebl138/rpg-7/main/media/first-feature.png)

- __Flexibility in choice__

  - There are three options which directly affect the strength and security of the passwords, ranging from least secure 
    (8 characters, no special characters, non-passphrase) to most secure (25 characters, including special characters, and 
    made up of a passphrase).

- __Save to Google Drive__

  - There is an option to save the generated password(s) to a file in Google Drive, from where they can be saved as a local 
    file to the user's computer.
  - Example of content of file saved in Google Drive with command '12,Y,Y,4,Y':

![Second feature](https://raw.githubusercontent.com/ebl138/rpg-7/main/media/second-feature.png)

### Future features

- Make passphrase passwords grammatically correct and sensical and, thus, easier to remember
- Substitute out more letters for numbers
- Insert more capital letters into passphrases

## Data model

## Testing

### Bugs

#### Solved bugs

#### Remaining bugs

- There are no (known) bugs remaining

### Validator testing

- No errors are returned when running run.py code through Code Institute's validator: https://pep8ci.herokuapp.com/

## Deployment

## Credits
