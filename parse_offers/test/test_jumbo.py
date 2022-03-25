import unittest

import jumbo

collection = jumbo.returnOffers()

class TestJumbo(unittest.TestCase):

    def test_return_list_jumbo(self):
        """
        ✅ Jumbo geeft aanbiedingen terug 👉 
        """
        collectionLength = len(collection)
        self.assertTrue(collectionLength != 0) # jumbo geeft resultaten terug

    def test_list_has_product_title(self):
        """
        ✅ Alle Jumbo aanbiedingen hebben een titel 👉 
        """
        for item in collection:
            self.assertTrue(item['product'] != '') # Item heeft een titel

    def test_list_has_product_deal(self):
        """
        ✅ Alle Jumbo aanbiedingen hebben een deal 👉 
        """
        for item in collection:
            self.assertTrue(item['deal'] != '') # Item heeft een deal

    def test_list_has_product_date_start(self):
        """
        ✅ Alle Jumbo aanbiedingen hebben een startdatum 👉 
        """
        for item in collection:
            self.assertTrue(item['dateStart'] != '') # Item heeft een startdatum

if __name__ == '__main__':
    unittest.main(verbosity=0)
