from itertools import chain
import random

def zlicz():
    numbers = [round(random.uniform(0,100))for i in range (10)]
    numbers2 = [round(random.uniform(0,100))for i in range (10)]
    
    for i in numbers2:
        numbers.append(i)
    numbers.sort()
    print(numbers)
zlicz()