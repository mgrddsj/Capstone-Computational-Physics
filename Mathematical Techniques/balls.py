#%%
import random

def allTheSame(list):
    for i in list:
        if i != list[0]:
            return False
    return True

def replecement(blue, red, times):
    pool = []
    result = []
    for i in range(0, red):
        pool.append("R")

    for i in range(0, blue):
        pool.append("B")

    for i in range(0, times):
        result.append(random.choice(pool))
    
    if(allTheSame(result)):
        return 1
    else:
        return 0

def withoutReplacement(blue, red, times):
    pool = []
    result = []
    for i in range(0, red):
        pool.append("R")

    for i in range(0, blue):
        pool.append("B")

    for i in range(0, times):
        ans = random.choice(pool)
        result.append(ans)
        pool.remove(ans)
    
    if(allTheSame(result)):
        return 1
    else:
        return 0

re = []
withoutRe = []
for i in range(1, 1000001):
    re.append(replecement(3, 3, 3))
    withoutRe.append(withoutReplacement(3, 3, 3))

print("The probability for the replacement situation is ", re.count(1)/len(re))
print("The probability for the withoutReplacement situation is ", withoutRe.count(1)/len(withoutRe))

