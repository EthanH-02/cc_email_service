# CompClub Emailing Service

## Table of contents
1. [About this Project](#About)
    1. [Initial Problem](#Initial_Problem)
    2. [Testing Application Integration](#Integration)
    3. [Quick Scripting](#Scripting)
3. [How to Use](#Use)
4. [Version History](#History)
5. [Goals](#Goals)

## About this Project <a name="About"></a>
Writting the implementation and structure of code to be utilised by the CompClub team in sending out emails about upcoming events and information.

### Initial Problem <a name="Initial_Problem"></a>
CompClub is a society at UNSW, that focuses on providing free educational content to highschool students. As such we have a budget for how much money we can possibly send and one of the central concerns was the fact that current providers on the market have a subscription model, which unfortunately is not sustainable for the rate of growth of the society. As such I realised we could probably write a script that could be used to send an email out automated from a table without having to worry about spending the excess sum of money on the serivce.

### Testing Application Integration <a name="Integration"></a>
As CompClub uses gmail to send and recieve all of its email content, it was essential to us to ensure that we can get it working on our system and functioning within time. Thus the application provides a strong example of practical coding use in the ability to integrate with other platforms. The overall goal is to make this email service undifferentiable from if we were to send individual emails out to each person.

### Quick Scripting <a name="Scripting"></a>
Along with the situation above, it is also crucial to be able to push this program out as soon as possible due to upcoming workshops. Ensuring the basic functionality is critical as to trust and run the program to send out information regarding the upcoming workshops with 3-4 weeks to spare on the content within them.

## How to Use <a name="Use"></a>
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
12. The terminal will show the details of the message about to be sent. Input 'Y' if you wish to proceed or 'N' if you wish to cancel the email

> NOTE: within ```./edit_content/email_contents.txt``` you can add custom edits to the email by utilising { } and putting the column title in between the braces. i.e. "Hello {name}" would be changed to "Hello John" in the email.

## Exemplar CSV

A CSV (Comma-Seperated Values) file is a formatting method that we can utilise to represent a table, where we denote different columns with commas and new lines as rows. When given the following table, it can be represented as both the table and the CSV.

| Character Name    | email                       | Book                       | Actor         |
|-------------------|-----------------------------|----------------------------|---------------|
| Frodo Baggins     | frodo2968@the_shire.com     | The Fellowship of the Ring | Elijah Wood   |
| Bilbo Baggins     | bilbo_baggins@the_shire.com | The Hobbit                 | Ian Holm      |
| Legolas Greenleaf | legolas_@sindar_elf.com     | The Fellowship of the Ring | Orlando Bloom |
| Éowyn             | eowyn@rohan.com             | The Two Towers             | Miranda Otto  |

```csv
Character Name,Email,Book,Actor
Frodo Baggins,frodo2968@the_shire.com,The Fellowship of the Ring,Elijah Wood
Bilbo Baggins,bilbo_baggins@the_shire.com,The Hobbit,Ian Holm
Legolas Greenleaf,legolas_@sindar_elf.com,The Fellowship of the Ring,Orlando Bloom
Éowyn,eowyn@rohan.com,The Two Towers,Miranda Otto
```

This is useful if we wanted to write a custom email we would be able to by going into ```./edit_content/email_contents.txt``` and changing it to the following.
```txt
Hello {actor}, I really enjoyed your potrayal of {character name}. It capsured their essence in {book}.
```

Taking the first row this would then send through an email that looks like the following below:
```txt
Hello Elijah Wood, I really enjoyed your potrayal of Frodo Baggins. It capsured their essence in The Fellowship of the Ring.
```

## Version History <a name="History"></a>
- ```v0.1.2``` Bug Fixes
    - Fixed bug in which emails were only being sent to the first user and crashing
- ```v0.1.1``` Optimisation & Refactoring Patch
    - Code functions faster by precomputing generic parts of the email before attaching more specifics
    - Backend cleaned up for smoother easier to understand
    - Reduced repeated calls to functions instead focusing on doing a single call
    - Reduced over sending information (i.e. sending in the list of emails directly instead of the list of recipient dictionary)
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

## Goals <a name="Goals"></a>
- [x] ~~Create a basic service that can send an email~~ ```Achieved: 23-05-2023```
- [x] ~~Create a service that can iterate through a list of emails to send them off~~ ```Achieved: 26-05-2023```
- [x] ~~Implement error messages to ensure code functions as expected~~ ```Achieved: 27-05-2023```
- [x] ~~Implement the ability to send files within the email service~~ ```Achieved: 28-05-2023```
- [ ] Add email signatures
- [ ] The ability to BCC in individuals
- [ ] Schedule sending emails
- [ ] Utilise the code in sending workshop information
- [ ] Send emails with bold, italics, underline and colour formatting
- [ ] Implement a front end to be utilised by the team so they don't have to worry about touching this GitHub

