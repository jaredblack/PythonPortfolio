# Generate random numbers between 1 - 12 to help me memorize the guitar fretboard

import random
def generate():
    oneTwelve = list(range(1,13))
    print(oneTwelve)
    scramble = random.shuffle(oneTwelve)
    for num in oneTwelve:
        print(num)

if __name__ == '__main__':
    generate()
