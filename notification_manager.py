import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

class NotificationManager:

    def send_mail(max_price):
        message = "Subject: iPad Pro Price Alert\n\n"
        message += f"Price just dropped below your maximum {max_price} SEK. Check it out:\n\n"
        message += "https://www.amazon.se/-/en/dp/B0BJNX5XFC/ref=sr_1_4?crid=1DALRNWFKVEYS&keywords=ipad%2Bpro&qid=1666786931&qu=eyJxc2MiOiI1LjAwIiwicXNhIjoiNC43NiIsInFzcCI6IjQuMTYifQ%3D%3D&refinements=p_85%3A20692917031%2Cp_n_feature_fourteen_browse-bin%3A28396975031&rnid=28396971031&rps=1&s=computers&sprefix=ipad%2Bpro%2Caps%2C192&sr=1-4&th=1"

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.environ.get("MY_EMAIL"), password=os.environ.get("MY_PASSWORD"))
            connection.sendmail(
                from_addr=os.environ.get("MY_EMAIL"),
                to_addrs=os.environ.get("SEND_TO"),
                msg=message
            )
