import pandas as pd
import datetime
import smtplib

# Enter your authentication details
GMAIL_ID = ""
GMAIL_PSWD = ""


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel("dates.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    print(yearNow)
    writeInd = []

    for index, item in df.iterrows():
        bday = item["Birthday"].strftime("%d-%m")
        msg = "hello"
        if today == bday and yearNow not in str(item["Year"]):
            sendEmail(
                item["Email"], "Happy Birthday" + " " + item["Name"], item["Dialog"]
            )
            writeInd.append(index)
    for i in writeInd:
        yr = df.loc[i, "Year"]
        df.loc[i, "Year"] = str(yr) + "," + str(yearNow)
    df.to_excel("dates.xlsx", index=False)
