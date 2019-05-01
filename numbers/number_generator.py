import random

def int_pair_generator(minVal1,maxVal1,minVal2,maxVal2):
    """
    This is an infinite number generator. It is up to the user when to stop.
    """
    while True:
        val1 = random.randint(minVal1,maxVal1)
        val2 = random.randint(minVal2,maxVal2)
        yield (val1,val2)
