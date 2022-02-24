import unittest

import jumbo

class TestJumbo(unittest.TestCase):

    def test_return_list_jumbo(self):
        """
        ✅ Jumbo geeft aanbiedingen terug 👉 
        """
        collectionLength = len(jumbo.returnOffers())
        self.assertTrue(collectionLength != 0) # jumbo geeft resultaten terug    

if __name__ == '__main__':
    unittest.main(verbosity=0)
