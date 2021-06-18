#### make list from txt file
### setup email to send to jmkobayashi6@gmail.com
### setup date of when to send the email using date_time
import smtplib
from random import choice
import datetime as dt
import math

email_receiver = "natasha_c@shaw.ca"
email_sender = "jmkobayashi8@gmail.com"
password = "Pandabear7!"
quote_list = []
with open("quotes.txt") as file:
    contents = file.readlines()
    quote = choice(contents)



time = dt.datetime.now()
weekday=time.weekday()


if weekday == 3:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password)
        connection.sendmail(from_addr=email_sender, to_addrs=email_receiver, msg=f"Subject: Inspirational "
                                                                                 f"Quote\n\n{quote}")
        connection.close()



