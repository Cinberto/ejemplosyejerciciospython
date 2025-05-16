#función cuenta
import time

def countdown(n):
    while n >= 0:
        print(n)
        time.sleep(1)
        n -= 1

countdown(25)
print("tu comida ya esta lista!")
