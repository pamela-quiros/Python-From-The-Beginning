#1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random

randon_number = random.random()
random_number_2 = random.randint(1, 10)
print(randon_number)
print(random_number_2)

#2) Use the datetime library together with the random number to generate a random, unique value.
import datetime

random_unique = str(randon_number) + str(datetime.datetime.now())
print(random_unique)