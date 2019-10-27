import random

def start_playground():
    return [[random.choice((1,2,3,4)) for x in range(11)] for y in range(11)]
def print_playground():
    temp = zip(*reversed(playground))
    for rand in temp:
        print(rand)

playground = start_playground()
print_playground()