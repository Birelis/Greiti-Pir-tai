import time

def inputas():
    start = time.time()
    val = input()
    end = time.time()
    difference = end - start
    return val, difference
