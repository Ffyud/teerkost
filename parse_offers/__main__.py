import albertheijn
import jumbo
import json
import shutil


if __name__ == "__main__":
    jumboOffers = jumbo.returnOffers()
    ahOffers = albertheijn.returnOffers()

    allOffers = jumboOffers + ahOffers

    with open('offers.json', 'a+', encoding='utf-8') as f:
            json.dump(allOffers, f, indent=4,ensure_ascii = False)

    shutil.move('offers.json', 'kortings-app/src/offers.json')
