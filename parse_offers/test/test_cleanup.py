import unittest

from cleanup import categorize

class TestCleanup(unittest.TestCase):

    def test_return_category_by_title(self):
        """
        ✅ Categorie voor product wordt gevonden in titel 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("bier water", "een flesje")

        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_by_description(self):
        """
        ✅ Categorie voor product wordt gevonden in beschrijving 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("een flesje", "water bier")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_by_title_w_minus(self):
        """
        ✅ Categorie voor product wordt gevonden in beschrijving met minteken 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("een flesje", "bier-klein-bier")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_by_description_w_minus(self):
        """
        ✅ Categorie voor product wordt gevonden in titel met minteken 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("flesje-bier-groot", "een flesje")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_w_empty_title(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende titel 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("", "bier")
        self.assertTrue(resultingCategory == 'bier')    
    
    def test_return_category_w_empty_description(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende beschrijving 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("bier", "")
        self.assertTrue(resultingCategory == 'bier')   

    def test_return_empty_w_empty_input(self):
        """
        ✅ Categorie voor product wordt leeg teruggegeven bij lege titel input 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("", "")
        self.assertTrue(resultingCategory == '') 

    def test_return_empty(self):
        """
        ✅ Categorie voor product wordt leeg teruggegeven bij onbekend product 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("niets", "niks")
        self.assertTrue(resultingCategory == '')          

if __name__ == '__main__':
    unittest.main(verbosity=0)
