import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get("https://scrapingclub.com/exercise/list_basic/?page=1")
print(response.text)

soup = BeautifulSoup(response.text, "lxml") #html.parser

data=soup.find_all("div", class_= "col-lg-4 col-md-6 mb-4")

for i in data:

    name= i.find("h4",class_="card-title").text.replace("/n","")

    #print(name)

    price = i.find("h5").text

    #print(price)

    url_img = "/static/img/90008-E.jpg" + i.find("img",class_="card-img-top img-fluid").get("src")

    #print(url_img)

    print(name + "\n" + price + "\n" + url_img + "\n\n")