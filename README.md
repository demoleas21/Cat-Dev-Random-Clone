# Cat Dev Random Clone

## Description
The command `cat /dev/random` is used to generate entropy until a file becomes so large the disc runs out of space. This is a python 3.10.2 copy of this linux command. The script uses time seeds to generate randomness and to offset the speed of python's execution it uses bit manipulation to add more randomness to the characaters generated.

## Usage
The script can be executed by cloning or downloading the file and running the following command:

`python {path}/run.py [limiter]`

Conversely you may change directory to the location of the file and run without a path entered.

The limiter is used to limit the number of times python hits the time api to avoid looping forever until the disc is out of space.

### *Warning:*
It is not recommended to run this script without a limiter unsupervised as it can become extremely large and fill your entire disc drive. When using the limiter numbers larger than 10000 begin to create longer run times. Each loop through the time api is longer than the last and the time is not linear for increasing limiters.
