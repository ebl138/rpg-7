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

## Testing

The program has been manually tested:

 - Passed run.py code through Code Institute's validator
 - Given invalid inputs for each option: strings when integers expected, integers when strings expected and numbers 
   outwith required ranges
 - Tested in vscode terminal and Heroku terminal

### Bugs

#### Solved bugs

- During development, in generate_passphrase(), when building the list of characters which becomes the password, I 
  appended the two letter word instead of each letter of the two letter word; this sometimes produced a password 
  with incorrect length e.g. a 21 character password when a 20 character password was requested. This was fixed 
  by appending each character of the word, instead of the word itself

#### Remaining bugs

- There are no (known) bugs remaining

### Validator testing

- No errors are returned when running run.py code through Code Institute's validator: https://pep8ci.herokuapp.com/

## Deployment

IMPORTANT NOTE REGARDING DEPLOYMENT:

- As you might have noticed already, I have uploaded the creds.json, client_secrets.json and settings.yaml to this 
  repo; as such, I haven't set any config vars in Heroku, except for CREDS, which is the content of my creds.json 
  file but I'm pretty sure this doesn't do anything for this project. I'm also aware these files expose sensitive 
  information regarding my Google account but, unfortunately, I couldn't find any other way to make this work. You 
  may need to replace these files with the information of your own Google account to get the fifth (saving to Google 
  Drive) feature to work; alternatively, you can use the provided files and this will create a file in my Google Drive.
- If you need to test with your own/a Code Institute Google account, you can create these files by doing the following:
    1. Go to Google Developers Console - https://console.developers.google.com and create a new project. Click on 
    Enable and manage APIs, click on Drive API, then click on Enable API. In API Manager, click on Credentials on 
    the left panel. Select Add Credentials, choose OAuth 2.0 client ID, then Web Application. You may need to configure 
    a consent screen, where the required part is the Product name, and the rest you can leave blank. In the Create client 
    ID window, with Web application selected as Application type, specify the Name for your application, put 
    http://localhost:8080 for Javascript origins and http://localhost:8080/ for redirect URIs. IMPORTANT: One of these ends 
    with /, the other does not.
    2. Go to Google Developers Console -https://console.developers.google.com and find the Use Google API section and 
    click on Enable and manage APIs. Select Credentials on the left panel. You should see a list of your OAuth 2.0 client 
    IDs. Check off the one you've created in step 1, and click on the download JSON button (looks like an arrow down icon). 
    Rename the downloaded file to client_secrets.json.
    3. You may find using a settings.yaml file useful for easier/quicker authentication; just copy mine and replace the 
    client_id and client_secret fields with those of your own account. They can be found in the client_secrets.json file 
    downloaded in the previous step.
    4. You will probably be asked to authenticate when testing out the 'Save to Google Drive' functionality for the first 
    time; this should open a browser and you will need to follow the instructions to allow the app access to your Google 
    Drive, etc. After this, however, you shouldn't need to manually authenticate again.
    5. If I missed out any steps/information here, sorry, I found most of this information from this Stack Overflow answer: 
    https://stackoverflow.com/questions/28184419/pydrive-invalid-client-secrets-file. Hopefully it helps

### How to deploy

- Fork or clone this repository
- Create a new Heroku app
- Set the buildpacks to Python and NodeJS in that order
- Link the Heroku app to the repository by clicking Github then entering name of repository
- Click on Enable Automatic Deploys then Open app (top right)

## Credits

- Code Institute for the template on Github on which I based my project, including the mock terminal for Heroku
- the Faker module (https://faker.readthedocs.io/en/master/)
- the PyDrive module (https://pypi.org/project/PyDrive/)