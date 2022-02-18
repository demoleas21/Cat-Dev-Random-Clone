import sys
from dev_random import devRandom


def main():
	limiter = sys.argv[1] if len(sys.argv) > 1 else None
	try:
		limiter = int(limiter) if limiter else None
		devRandom(limiter)
	except ValueError:
		print('Error: Value entered is not an integer')


main()
