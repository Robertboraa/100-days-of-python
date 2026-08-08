import smtplib
import random
from datetime import datetime
import schedule
import time
import pandas
import csv
import os
##################### Hard Starting Project ######################
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
my_email = "denemebora1234@gmail.com"
password = "pwro gbcb kviy bptx"
with open('birthdays.csv', 'r') as f:
    reader = csv.DictReader(f)
    my_dict = {row["name"]: {"month": row["month"], "day": row["day"],"email ":row["email"]} for row in reader}
month = str(datetime.now().month)
day = str(datetime.now().day)
print(my_dict)





# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
# #     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
for name, data in my_dict.items():
    if data["month"] == month and data["day"] == day:
        print(f"Today is {name}'s birthday!")

        templates = []
        for filename in os.listdir("letter_templates"):
            with open(f"letter_templates/{filename}", encoding="latin-1") as f:
                templates.append(f.read())

        birthday_message = random.choice(templates).replace("[NAME]", name)

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=data["email "],
                msg=f"Subject: Happy Birthday!\n\n{birthday_message}"
            )

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com











