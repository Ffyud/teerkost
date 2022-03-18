import albertheijn
import jumbo
import lidl
import json
import shutil
import requests
from PIL import Image
import os
import time
import uuid

def updateImageUrlForOffer(url, offer):
    """Update the field for image in the json object"""

    print("     ✅ Update de locatie van de afbeelding: " + url)
    offer.update({"image": url})


def tryAndSaveTheImage(url, destination):
    """Tries to download and save the image and convert it to webp format."""

    domain = "https://teerkost.nl/img/"
    resultingUrl = url

    try:
        response = requests.get(imageUrl,timeout=5)

        if response.status_code == 200:
            imageData = requests.get(imageUrl, headers=headers).content
            newFileName = str(uuid.uuid4().hex)

            try:
                with open(destination + '/'+ newFileName +'.png', 'wb') as i:
                    i.write(imageData)
                    print("     ✅ Afbeelding " + newFileName + " opslaan.")
                    
                    try:
                        img = Image.open(destination + '/' + newFileName +'.png')
                        img.save(destination + '/'+newFileName+'.webp', format="webp")
                        print("     ✅ Afbeelding geconverteerd naar webp.")
                        resultingUrl = domain + '' + newFileName + '.webp'
                        os.remove(destination + '/' + newFileName + '.png')
                    except Exception as e:
                        print("     " + e)
                        print("     🤔 Converteren naar webp mislukt, we blijven bij png.")
                        resultingUrl = domain + '' + newFileName + '.png'
            except Exception as e:
                print("     🟥 Opslaan lijkt mislukt.")
                print("         " + e)
        else:
            print("     🟥 Antwoord " + str(response.status_code) + " teruggekregen.")
    except requests.exceptions.Timeout:
        print("     🟥 Helemaal mis!")
            
    return resultingUrl

def moveFolder(folderPath, destination):
    """Moves the provided folder to the destination."""

    print(" ")
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print("✅ Folder " + folderPath + " bestaat op " + destination + " -> inhoud verwijderen.")

    shutil.move(folderPath, destination)
    print("✅ Folder " + folderPath + " uit project verplaatsen naar " + destination + ".")


def moveFile(file, destination):
    """Moves the provided file to the destination."""

    print("✅ Verplaats " + file + " uit het project naar " + destination + ".")
    shutil.move(file, destination + file)

if __name__ == "__main__":

    take_it_easy = 2

    jumboOffers = jumbo.returnOffers()
    ahOffers = albertheijn.returnOffers()
    lidlOffers = lidl.returnOffers()

    allOffers = jumboOffers + ahOffers + lidlOffers
    allOffers = sorted(allOffers, key=lambda p: p['category'])

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
        }

    print("🟢 Er zijn "+str(len(allOffers))+" aanbiedingen gevonden.")
    time.sleep(take_it_easy)
    print(" ")
    print("✊ Aan de slag met afbeeldingen downloaden en converteren naar webp.")
    print(" ")
    time.sleep(take_it_easy)

    try:
        shutil.rmtree('parse_offers/img')
        print("     ✅ Img folder met inhoud verwijderen uit het project.")
    except FileNotFoundError:
        print("     🤔 Geen img folder gevonden in dit project om te verwijderen.")
    
    print (" ")
    os.mkdir('parse_offers/img')
    print("     ✅ Schone img folder gemaakt in het project.")
    print(" ")

    time.sleep(take_it_easy)
    index = 0    
    try:
        for offer in allOffers:
            print("     🔎 Afbeelding " + str(index+1))
            index = index+1
            imageUrl = offer['image']
            destination = 'parse_offers/img'
            resultingUrl = tryAndSaveTheImage(imageUrl, destination)
            updateImageUrlForOffer(resultingUrl, offer)

    except Exception as e:
        print(e)

    time.sleep(take_it_easy)

    moveFolder('parse_offers/img', 'kortings-app/public/img')

    time.sleep(take_it_easy)
    print(" ")
    print("✅ Dump de aanbiedingen in een JSON bestand.")
    with open('offers.json', 'a+', encoding='utf-8') as f:
            json.dump(allOffers, f, indent=4,ensure_ascii = False)
    
    moveFile('offers.json', 'kortings-app/src/')
