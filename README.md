# cc_email_service

## about_this_project
Writting the implementation and structure of code to be utilised by the CompClub team in sending out emails about upcoming events and information.

The cause of this problem was the factor that certain service's subscription model's are not sustainable enough for us to utilise as a society considerign the limited budget we posses.

The code works with gmail in order to be able to send mass emails about upcoming events within the program.

## how_to_use
> **RIGHT NOW THE CODE WILL NOT FUNCTION AS IMPLEMENTATION HAS NOT BEEN CREATED**
1. Create a copy of the code on your local device
2. Within edit content there are 3 files *THESE ARE TO BE THE ONLY FILES YOU EDIT*
3. Start by within email_info.txt changing the information regarding the email as required ```TO: to_email_address@gmail.com FROM: from_email_address@gmail.com SUBJECT: subject of the email``` Please note that you will have to keep the first elements [TO:, FROM:, SUBJECT:] in order for the email to work
4. Within email_contents.txt edit the infomration so that the contents match as you would require
5. Within sensative_info.py please implement the email account name you wish to send from and create an app password for gmail
6. Run the main.py code and the emails should be ready to be sent

## goals
1. Create a basic service that can send an email
2. Create a service that can iterate through a list of emails to send them off
3. Utilise the code in sending workshop information
4. Send complex emails such as those with file attachments, images, bold text etc.
5. Implement a front end to be utilised by the team so they don't have to worry about touching this GitHub

