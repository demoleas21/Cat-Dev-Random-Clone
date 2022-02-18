import datetime
import math
import string


def devRandom(limiter=None):
	"""
	Creates file with randomized ascii characters until keyboard interupt or character limit is reached

	:param int limiter: Limits the number of times the time function is hit to stop random generation
		Bit shifting causes increasingly long loops, do not expect linear time growth as limiter is increased
	"""
	bitShifter = 0
	randomText = ''
	keepRunning = True
	write(randomText)
	while keepRunning:
		for randomNumber in timeRandomizer(bitShifter):
			randomText += string.printable[randomNumber % 100]
		if limiter and bitShifter >= limiter:
			keepRunning = False
		bitShifter += 1
		write(randomText, append=True)
		randomText = ''


def timeRandomizer(bitShifter):
	"""
	Time based randomization that uses milliseconds offset by time and date to create more unique seeds
	Uses bit manipulation to prevent minor mllisecond changes that create patterns

	:param int bitShifter: Shifts the bits of the time seed to dramitically randomize each millisecond change
	:return list: Numbers ranging from 0-100 that can be converted to the 100 ascii characters
	"""
	# Uses all intervals of date and time other than milliseconds and aggregates to create a unique offset
	dateAggregation = sum(
		[int(interval) for interval in datetime.datetime.now().strftime('%S %M %H %d %m %y').split()]
	)
	# Uses milliseconds and shifts the bits to handle python's execution speed to prevent patterns
	timeOffset = (int(datetime.datetime.now().strftime('%f')) + dateAggregation) << bitShifter
	randomNumbers = []
	# Reduces the time into chunks of integers from 0-100 to map to each ascii character
	while timeOffset >= 100:
		randomNumbers.append(timeOffset % 100)
		timeOffset = timeOffset // 100
	randomNumbers.append(timeOffset)
	return randomNumbers


def write(text, append=False):
	"""
	Create and write to a file with the option to overwrite or append to the existing file

	:param str text: String of characters to be written to the file
	:param bool append: Used to determine if we should overwrite or append to the existing file
	"""
	with open('dev_random.txt', 'a' if append else 'w') as f:
		f.write(text)
