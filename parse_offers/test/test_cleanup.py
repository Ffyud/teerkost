import unittest
import xmlrunner
from cleanup import categorize, cleantext, giveid

class TestCleanup(unittest.TestCase):

    def test_return_category_but_ignore_words(self):
        """
        β Categorie voor product vinden maar ook woorden negeren π 
        """
        resultingCategory = categorize.findCategoryForProduct("een biefstuk", "bla bla")
        self.assertTrue(resultingCategory == 'vlees')

        resultingCategory = categorize.findCategoryForProduct("een vegan", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.findCategoryForProduct("een vegan biefstuk", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.findCategoryForProduct("een biefstuk vegan", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.findCategoryForProduct("een biefstuk vegan biefstuk", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.findCategoryForProduct("calvΓ© saus", "bla bla")
        self.assertTrue(resultingCategory != 'beleg')

    def test_return_category_by_title(self):
        """
        β Categorie voor product wordt gevonden in titel π 
        """
        resultingCategory = categorize.findCategoryForProduct("bier water", "een flesje")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_by_description(self):
        """
        β Categorie voor product wordt gevonden in beschrijving π 
        """
        resultingCategory = categorize.findCategoryForProduct("een flesje", "water bier")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_w_empty_title(self):
        """
        β Categorie voor product wordt gevonden met ontbrekende titel π 
        """
        resultingCategory = categorize.findCategoryForProduct("", "bier")
        self.assertTrue(resultingCategory == 'bier')    
    
    def test_return_category_w_empty_description(self):
        """
        β Categorie voor product wordt gevonden met ontbrekende beschrijving π 
        """
        resultingCategory = categorize.findCategoryForProduct("bier", "")
        self.assertTrue(resultingCategory == 'bier')   

    def test_return_single_word_capitalized(self):
        """
        β Categorie voor product wordt gevonden met enkel woord en hoofdletter π 
        """        
        resultingCategory = categorize.findCategoryForProduct("Lenor", "derp derp")
        self.assertTrue(resultingCategory == 'huishouden')

    def test_return_single_word_w_apostrof(self):
        """
        β Categorie voor product wordt gevonden met enkel woord en apostrof π 
        """        
        resultingCategory = categorize.findCategoryForProduct("Mango's Ready to Eat", "2-pack")
        self.assertTrue(resultingCategory == 'fruit')    

    def test_return_empty_w_empty_input(self):
        """
        β Categorie voor product wordt leeg teruggegeven bij lege titel input π 
        """
        resultingCategory = categorize.findCategoryForProduct("", "")
        self.assertTrue(resultingCategory == '') 

    def test_return_empty(self):
        """
        β Categorie voor product wordt leeg teruggegeven bij onbekend product π 
        """
        resultingCategory = categorize.findCategoryForProduct("niets", "niks")
        self.assertTrue(resultingCategory == '')

    def test_clean_title(self):
        """
        β Titel van een product is netjes π 
        """
        cleanTitle = cleantext.cleanUpTitle("Jumbo Alle AH bananen* met schil ")
        expectedTitle = "Bananen met schil"
        self.assertEqual(cleanTitle, expectedTitle)

    def test_clean_info(self):
        """
        β Productinfo van een product is netjes π 
        """
        cleanInfoText = cleantext.cleanUpInfo("Alle soorten 300 gram")
        expectedInfoText = "300 gram"
        self.assertEqual(cleanInfoText, expectedInfoText)    

        cleanInfoText = cleantext.cleanUpInfo("Bijv. de groene soort")
        expectedInfoText = ""
        self.assertEqual(cleanInfoText, expectedInfoText)    

    def test_give_id(self):
        """
        β Product van een eigen ID voorzien π 
        """
        testOfferObject = [{
            'product': 'Luxe stol',
            'productInfo': '1 kilo',
            'category': 'brood',
            'image': 'plaatje',
            'deal': 'β¬1 korting',
            'price': '1.99',
            'dateStart': '2022-04-11',
            'dateEnd': '2022-04-18',
            'link': 'linkje',
            'shop': 'lidl'
        }, {
            'product': 'Hero jam',
            'productInfo': 'Minder zoet',
            'category': 'beleg',
            'image': 'plaatje',
            'deal': 'op=op',
            'price': '1.49',
            'dateStart': '2022-04-11',
            'dateEnd': '',
            'link': 'linkje',
            'shop': 'lidl'
        }]

        testOfferObjectExpected = [{
            'product': 'Luxe stol',
            'productInfo': '1 kilo',
            'category': 'brood',
            'image': 'plaatje',
            'deal': 'β¬1 korting',
            'price': '1.99',
            'dateStart': '2022-04-11',
            'dateEnd': '2022-04-18',
            'link': 'linkje',
            'shop': 'lidl',
            'id': 1
        }, {
            'product': 'Hero jam',
            'productInfo': 'Minder zoet',
            'category': 'beleg',
            'image': 'plaatje',
            'deal': 'op=op',
            'price': '1.49',
            'dateStart': '2022-04-11',
            'dateEnd': '',
            'link': 'linkje',
            'shop': 'lidl',
            'id': 2
        }]

        addId = giveid.giveIdToOffers(testOfferObject)
        self.assertEqual(addId, testOfferObjectExpected)        

if __name__ == '__main__':
   unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="."),
        failfast=False,
        buffer=False,
        catchbreak=False,
        verbosity=1)
