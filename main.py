import random
import smtplib
import os

# Load quotes from a file
with open("quotes.txt", "r") as file:
    quotes = file.readlines()

def random_selection(quotes):
    return random.choice(quotes).strip()

# Fetch a random quote
random_quote = random_selection(quotes)

# Securely load email credentials from environment variables
my_mail = os.getenv("MY_EMAIL")
password = os.getenv("MY_EMAIL_PASSWORD")

# Create the email message
subject = "Love Dose Everyday"
body = (
    "Hello Bubu,\n\n"
    "Some beautiful lines for the most beautiful girl in the world.\n"
    f"Motivational quote: {random_quote}\n"
    "Always be happy and motivated <3.\n\n"
    "Byeee Love, Take care :)"
)
message = f"Subject:{subject}\n\n{body}"

# Send the email
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(my_mail, password)
    connection.sendmail(from_addr=my_mail, to_addrs="mukeshhanuman2002@gmail.com", msg=message)
