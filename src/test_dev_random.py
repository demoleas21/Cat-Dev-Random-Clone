import dev_random
from unittest import TestCase, mock


class DevRandomTests(TestCase):

	@mock.patch('dev_random.write')
	def testRandomDistribution(self, mockWrite):
		"""
		Tests that even distribution is present in the randomized characters
		There are 100 possible charaters and we expect an even distribution amongst them (1% for each character)
		The larger the sample size the closer we get to an even distribution
		Small sample of 7000 rounds to the tenth place to handle variations of 0.05% within a dataset
		"""
		dev_random.devRandom(limiter=7000)
		randomChars = ''.join([call[1][0] for call in mockWrite.mock_calls])
		distributionDict = {}
		for char in randomChars:
			distributionDict[char] = distributionDict[char] + 1 if distributionDict.get(char) else 1
		self.assertEqual(len(distributionDict.keys()), 100)
		randomSize = len(randomChars)
		distributionPercentages = [round(val / randomSize * 100, 1) for val in distributionDict.values()]
		for percent in distributionPercentages:
			self.assertEqual(percent, 1)

	def testTimeRandomizerNoBitShifting(self):
		"""Without bit shifting we expect 6 digits out of our adjusted time giving us 3 values between 0-100"""
		randomNumbers = dev_random.timeRandomizer(0)
		self.assertEqual(len(randomNumbers), 3)
		for randomNumber in randomNumbers:
			self.assertTrue(0 <= randomNumber <= 100)

	def testTimeRandomizerBitShifting(self):
		"""With bit shifting we increase the size of the adjusted time and expect more random values"""
		randomNumbers = dev_random.timeRandomizer(10)
		self.assertTrue(4 <= len(randomNumbers) <= 5)
		for randomNumber in randomNumbers:
			self.assertTrue(0 <= randomNumber <= 100)




