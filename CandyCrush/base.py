import random

def start_playground():
    playground = [[random.choice((1,2,3,4)) for x in range(11)] for y in range(11)]
    for rand in playground:
        print(rand)

start_playground()