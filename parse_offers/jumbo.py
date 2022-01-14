import requests
from datetime import datetime
  

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
        offer = {"product":"", "productInfo":"", "image":"", "deal":"", "price": 0, "dateStart":"", "dateEnd":"", "link": "", "shop":""}
        
        offer.update({"product": i['name']})
        offer.update({"productInfo": i['summary']})
        offer.update({"shop": SHOP})
        # if('price' in i):
        #     offer.update({"price": i['price']['now']})
        
        offer.update({"deal": i['tag']})
        offer.update({"image": i['promotionImage']['main']})


        startDate = datetime.fromtimestamp(i['fromDate']/1000).strftime('%Y-%m-%d')
        endDate = datetime.fromtimestamp(i['toDate']/1000).strftime('%Y-%m-%d')
        offer.update({"dateStart": str(startDate)})
        offer.update({"dateEnd": str(endDate)})
        
        offer.update({"link": "https://jumbo.com/aanbiedingen/" + i['id']})
        collection.append(offer)

    return collection