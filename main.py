import requests
from apikey import API_TOKEN
#params = {"q": "London", "appid" : API_TOKEN, "units": "metric"}

data = {"custname": "artur","custtel":"79059059000","custemail":"dart@yandex.ru",
"size":"medium",
"topping":"bacon",
"delivery":"","comments": "" ,}



headers ={
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Referer": "http://httpbin.org/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-63defc53-248a5e68078424ae0d29d471"
  }

variable=requests.Session()

au_k = variable.get("https://github.com")

response =variable.post("https://github.com", headers=headers, data=data)


#print(response.status_code)
#print(response.headers)
print(response.text)

