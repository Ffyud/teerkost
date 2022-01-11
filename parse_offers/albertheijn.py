import requests
import json
import datetime
  
SHOP = "AH"

URL = "https://www.ah.nl/bonus/api/segments?segmentType=-PREMIUM"
  
r = requests.get(url = URL)
  
data = r.json()

collection = []

for i in data['collection']:
    offer = {"product":"", "productInfo":"", "deal":"", "price": 0, "dateStart":"", "dateEnd":"", "link": "", "shop":""}
    offer.update({"product": i['title']})
    offer.update({"productInfo": i['description']})
    offer.update({"shop": SHOP})
    if('price' in i):
        offer.update({"price": i['price']['now']})
    
    if('shields' in i):
        shield = i['shields'][0]['text']
        toString = " ".join(str(x) for x in shield)
        offer.update({"deal": toString })

    href = i['href']
    weekNumber = href.split("week=")[-1]
    now = datetime.datetime.now()
    startDate = datetime.date.fromisocalendar(now.year, int(weekNumber), 1)
    endDate = datetime.date.fromisocalendar(now.year, int(weekNumber), 7)
    offer.update({"dateStart": str(startDate)})
    offer.update({"dateEnd": str(endDate)})
    
    offer.update({"link": "https://ah.nl" + i['href']})
    collection.append(offer)


with open('offer-'+ SHOP + '.json', 'w', encoding='utf-8') as f:
    json.dump(collection, f, indent=4,ensure_ascii = False)    