import random
test = [1,0,2,0,4]
print(test)
test = list(filter(lambda x: x != 0, test))

test[0:0] = 2 * random.sample([1,2,3,4], 1)
print(test)