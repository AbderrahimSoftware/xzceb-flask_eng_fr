import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
      def testEnglishToFrenchNull(self):
         self.assertEqual(englishToFrench(None), None)

      def testFrenchToEnglishNull(self):
         self.assertEqual(frenchToEnglish(None), None)

      def testEnglishToFrenchHello(self):
         self.assertEqual(englishToFrench("Hello"), "Bonjour")

      def testFrenchToEnglishHello(self):
         self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
	
if __name__ == '__main__':
      unittest.main()
