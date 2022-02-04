import requests
from datetime import datetime
import categorize
  

def returnOffers():
    SHOP = "Jumbo"
    URL = "https://mobileapi.jumbo.com/v17/promotions"
    
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

    r = requests.get(url=URL, headers=HEADERS)
    
    data = r.json()

    collection = []

    for i in data['sections'][0]['current']['promotions']:
        offer = {"product":"", "productInfo":"", "category":"", "image":"", "deal":"", "price": 0, "dateStart":"", "dateEnd":"", "link": "", "shop":""}
        
        offer.update({"product": i['name']})
        offer.update({"productInfo": i['summary']})

        category = categorize.findCategoryForProduct(i['name'], i['summary'])
        offer.update({"category": category})

        offer.update({"shop": SHOP})

        deal = i['tag']
        offer.update({"deal": deal})
        if "voor € " in deal: # indien "voor €" wordt gevonden kan de prijs bepaald worden
            deal = deal.split("voor € ")
            price = deal[1]
            offer.update({"price": price.replace(",", ".")})

        offer.update({"image": i['promotionImage']['main']})

        startDate = datetime.fromtimestamp(i['fromDate']/1000).strftime('%Y-%m-%d')
        endDate = datetime.fromtimestamp(i['toDate']/1000).strftime('%Y-%m-%d')
        offer.update({"dateStart": str(startDate)})
        offer.update({"dateEnd": str(endDate)})
        
        offer.update({"link": "https://jumbo.com/aanbiedingen/" + i['id']})
        collection.append(offer)

    return collection