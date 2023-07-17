#monday motivational quotes

import smtplib
import datetime as dt
import random


my_email = ""
my_password = "" 


now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 0: #today
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Monday Motivation\n\n {quote}")
    