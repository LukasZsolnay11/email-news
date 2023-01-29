import requests
from send_email import send_email

api_key = "7378ab3ce0d5472d979a03072f7b312c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-29&sortBy=publishedAt&apiKey=7378ab3ce0d5472d979a03072f7b312c"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n"\
    + article["description"] + 2*"\n"

body=body.encode("utf-8")
send_email(message=body)
