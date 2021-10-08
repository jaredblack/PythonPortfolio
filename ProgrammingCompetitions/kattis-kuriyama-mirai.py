# Jared Black
# Solution to code challenge:
# https://codeforces.com/gym/348141/problem/B

import itertools

# Taking the necessary input
def solve():
    numStones = int(input())
    stoneCosts = [0]
    stoneCosts.extend([int(n) for n in input().split()])
    numQuestions = int(input())
    questions = []
    for i in range(numQuestions):
        questions.append([int(n) for n in input().split()])

    sumStones = list(itertools.accumulate(stoneCosts))
    stoneCosts.sort()
    sortSumStones = list(itertools.accumulate(stoneCosts))

    for question in questions:
        type = question[0]
        if type == 1:
            print(sumStones[question[2]] - sumStones[question[1] - 1])
        else:
            print(sortSumStones[question[2]] - sortSumStones[question[1] - 1])
    
if __name__ == '__main__':
    solve()
