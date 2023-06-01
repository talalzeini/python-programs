# pip install beepy
import beepy as beep

counter = 1
# repeat beep 10 times
while counter <= 10:
    print(counter)
    beep.beep(1)
    counter += 1