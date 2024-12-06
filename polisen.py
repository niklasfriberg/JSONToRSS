import requests
import time
from rfeed import *


try:
    with open("webserv/polisen.xml", "x") as f:
        pass
except FileExistsError:
    pass
url = "https://polisen.se/api/events"

while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Failed to retrieve data")
    items_ = []
    feed = rfeed.Feed(
        title="Polisens senaste",
        link="https://polisen.se",  
        description="Polisens senaste händelser",
        items=items_,
    )
    for item in data:
        items_.append(
            Item(
                title = item["name"],
                description = item["summary"],
                link = "https://polisen.se" + item["url"],
                guid = Guid("https://polisen.se" + item["url"])
            )
        )
    with open("webserv/polisen.xml", "w") as f:
        f.write(feed.rss())
    time.sleep(10)