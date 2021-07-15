import random

lower = "abcdefghjiklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!”#$%&'()*+,-./:;<=>?@[]^_`{|}~"
characters = lower + upper + numbers + symbols
password = "".join(random.sample(characters, random.randint(8, 25)))
print(password)