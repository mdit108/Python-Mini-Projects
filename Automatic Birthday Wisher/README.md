# Automatic Birthday Wisher

This project will help you to wish your friends a Happy Birthday using a Python script. The script can be scheduled to run everyday to automate the process.


Install pandas in Python before running the project
```Shell

pip install pandas

```

Steps to Configure the project to your local system to send e-mails to all your friends on their Birthday.

1. Enter your Gmail ID and Gmail Password in the top section in the designated space in the python file at the top.
    ```Python
    # Enter your authentication details
GMAIL_ID = ""
GMAIL_PSWD = ""
```

2. Enter details of the friends you want to send emails to in the dates.xlsx file. 
    - Sno : Enter the serial number starting from 1 for each entry.
    - Name : Enter the Name of the person 
    - Birthday : Enter the person's birthday in DD-MM-YYYY format. The spreadsheet will format it as required.
    - Dialog : Enter the message you want to send to the person.
    - Year : Leave empty while creating a new entry.
    - Email_To : Enter the email_id of the person.
3. Close the dates.xlsx file and run the python program
