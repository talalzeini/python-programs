import beepy as beep
# Install beepy using the following commands
# pip install beepy
# or
# python3 -m pip install beepy

counter = 1
# repeat beep 10 times
while counter <= 10:
    print(counter)
    beep.beep(1)
    counter += 1
