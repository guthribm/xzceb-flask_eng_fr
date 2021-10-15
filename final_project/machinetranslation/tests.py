import unittest
from translator import englishToFrench, frenchToEnglish

class TestMyTranslators(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test_englishToFrenchNull(self):
        self.assertIsNotNone(englishToFrench(None))
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    def test_frenchToEnglishNull(self):
        self.assertIsNotNone(frenchToEnglish(None))    

if __name__ == "__main__":
    unittest.main()
