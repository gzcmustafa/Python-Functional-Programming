import random
x=[1,2,3,"a","b"]

print(random.choice(x))

print(random.sample(x,2))

random.shuffle(x)
print(x)