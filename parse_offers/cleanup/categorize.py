import json
import sys
import os
import re

def findCategoryForProduct(title, description):

    CATEGORIES_JSON = os.path.join(os.path.dirname(__file__), "categories.json")

    with open(CATEGORIES_JSON, 'r') as jsonFile:
        data=jsonFile.read()

    categories = json.loads(data)
    
    wordsList = re.split(' |-', title.lower().replace(',', ''))
    descriptionWordList = re.split(' |-', description.lower().replace(',', ''))
    wordsList.extend(descriptionWordList)

    foundCategory = ""

    for word in wordsList:
        for k in categories:
            for keyword in k['keywords']:
                if keyword.lower() == word:
                    foundCategory = k['name']
    
    return foundCategory
