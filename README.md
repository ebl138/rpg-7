# RPG-7 Random Password Generator

RPG-7 is a Python terminal applicaton, which runs in the Code Institute mock terminal on Heroku.

Users can generate random password(s) as per their desired specification and receive these either as direct output 
from the terminal or have them saved to a document in Google Drive.

[Live version of the project](https://rpg-7-05e54012230e.herokuapp.com/)

![Am I Responsive mockup](https://raw.githubusercontent.com/ebl138/rpg-7/main/media/RPG-7-responsive-mockup.PNG)

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

## Features

- __Random, strong password generation__

- __Flexibility in choice__

- __Save to Google Drive__

### Existing features

### Future features

## Data model

## Testing

## Bugs

### Solved bugs

### Remaining bugs

### Validator testing

## Deployment

## Credits

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
