#A function can have multiple return statements. When any of them is executed, the function terminates.

import random
def randInt(min=0, max=100):
    num=(random.random()*(max-min)+min)
    return round(num)

a=randInt(min=5, max=200)
print(a)

    






    
    


