import unittest
import features
import numpy as np

class TestClassifyMethods(unittest.TestCase):
	def testTok(self):
		self.assertEqual(features.getTok("Hello my name is Bill"), ["Hello", "my", "name", "is", "Bill"])

	def testPOSTag(self):
		self.assertEqual(features.getTag("I am God"), [('I', 'PRP'), ('am', 'VBP'), ('God', 'NNP')])

	def testFeatureVector(self):
		self.assertEqual(features.main("I am God").tolist(), [0, 0, 0, 0, 0])
		self.assertEqual(features.main("Currently, 250 million fewer women than men are online globally. Bridging the digital gender gap is key to #WomensEconomicEmpowerment"), [0, 2, 1, 0, 0])

if __name__=="__main__":
	unittest.main()
