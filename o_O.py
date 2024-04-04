import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []

headers = {"User-Agent":
               "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (-NET CLR 3.5.30729)"}

for count in range(1, 7):

    sleep(3)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")  # html.parser

    data = soup.find_all("div", class_="w-full rounded border")

    for i in data:
        card_url = "https://scrapingclub.com" + i.find("a").get("href")
        list_card_url.append(card_url)






















        # name = i.find("h4").text.replace("\n", "")
        # price = i.find("h5").text
        # url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
        #
        # print(name + "\n" + price + "\n" + url_img + "\n\n")
