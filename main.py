from webscraper import Webscraper
from notification_manager import NotificationManager

MAX_PRICE = 18000.0

def main():
    current_price = Webscraper.get_current_price()
    if current_price <= MAX_PRICE : NotificationManager.send_mail(MAX_PRICE)

if __name__ == "__main__":
    main()
