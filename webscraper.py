import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.se/-/en/dp/B0BJNX5XFC/ref=sr_1_4?crid=1DALRNWFKVEYS&keywords=ipad%2Bpro&qid=1666786931&qu=eyJxc2MiOiI1LjAwIiwicXNhIjoiNC43NiIsInFzcCI6IjQuMTYifQ%3D%3D&refinements=p_85%3A20692917031%2Cp_n_feature_fourteen_browse-bin%3A28396975031&rnid=28396971031&rps=1&s=computers&sprefix=ipad%2Bpro%2Caps%2C192&sr=1-4&th=1"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7,no;q=0.6"
}


class Webscraper:

    def get_current_price():

        try:
            response = requests.get(url=URL, headers=HEADER)
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
        else:
            data = response.text
            soup = BeautifulSoup(markup=data, features="html.parser")
            price = soup.find(name="span", class_="a-price-whole").getText().replace(",", "")
            return float(price)