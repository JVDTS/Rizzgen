import random

def get_random_pickup_line(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

file_name = 'rizz.txt'
random_line = get_random_pickup_line(file_name)
print("Rizz Line:", random_line)
