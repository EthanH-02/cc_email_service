# CompClub Emailing Service

## About this Project
Writting the implementation and structure of code to be utilised by the CompClub team in sending out emails about upcoming events and information.

The cause of this problem was the factor that the optional service's subscription model's are not sustainable enough for us to utilise as a society considerign the limited budget we posses as a charity organisation that runs free workshops.

The code works with gmail in order to be able to send mass emails about upcoming events within the program.

## Version History
- ```v0.1.0``` Implemented the ability to share files through the email & bug fixes
    - Can share multiple files within the program by inserting them into the directory: ```./edit_content/files```
    - Bug fixes resolving a problem in which variables were not being changed in the emails content
- ```v0.0.1``` Implemented error checks and basic terminal feedback to ensure that the user is sending the information that they wish to send
    - Ensures user is signed in
    - Ensures user has implemented a link to a CSV file which has an email field
    - Ensures user has put edits into the document and isn't about to send an empty email out
    - Provides output of the email: sender, recipients, subject, content and asks for confirmation before sending
    - Provides output as each email is sent such that for longer services we can avoid worrying about the project crashing halfway through
    - Provides output when all emails are sent
- ```v0.0.0``` Basic functionality of code implemented able to be used to send a text file that can be edited within the project

## How To Use
1. Create a copy of the code on your local device
2. Within the directory ```./edit_content``` there are 3 files
    - ```./edit_content/email_info.txt```
    - ```./edit_content/email_content.txt```
    - ```./edit_content/sensative_info.py```
4. Start by adding your CSV file into the ```./edit_content``` directory
5. Now go into ```./edit_content/sensative_info.py``` and insert the gmail address you wish to send from into ```LOGIN_EMAIL```
6. Following this go to your Google Account settings and go ```Settings > Security > 2-Step Verification > App Passwords > Select App > Mail > Generate```. From here you take this password and enter it into ```LOGIN_PASSWORD``` in the same ```./edit_content/sensative_info.py```
7. Change the value of ```CSV_FILENAME``` to the path to the CSV file you have implemented within ```./edit_content/sensative_info.py```
8. Switch into ```./edit_content/email_info.txt``` and write your subject header file
9. Switch into ```./edit_content/email_contents.txt``` and write the message for your email
10. Add any files you wish to send in the email into the directory ```./edit_content/files```
11. Open a terminal in the directory and run ```./main.py```

> NOTE: within ```./edit_content/email_contents.txt``` you can add custom edits to the email by utilising { } and putting the column title in between the braces. i.e. "Hello {name}" would be changed to "Hello John" in the email.

## Goals
- [x] ~~Create a basic service that can send an email~~ ```Achieved: 23-05-2023```
- [x] ~~Create a service that can iterate through a list of emails to send them off~~ ```Achieved: 26-05-2023```
- [x] ~~Implement error messages to ensure code functions as expected~~ ```Achieved: 27-05-2023```
- [x] ~~Implement the ability to send files within the email service~~ ```Achieved: 28-05-2023```
- [ ] Schedule sending emails
- [ ] Utilise the code in sending workshop information
- [ ] Send emails with bold, italics, underline and colour formatting
- [ ] Implement a front end to be utilised by the team so they don't have to worry about touching this GitHub

