# My solution to this problem: https://open.kattis.com/problems/semafori

def getLightStatus(light, timeElapsed):
    distilled = timeElapsed % (light[1] + light[2])
    if distilled >= light[1]:
        return "Green"
    return "Red"


def solve(lights:list, road_length: int) -> int:
    timeElapsed = 0
    lastLightDist = 0
    for light in lights:
        timeElapsed += light[0] - lastLightDist
        while(getLightStatus(light, timeElapsed) == "Red"):
            timeElapsed += 1
        lastLightDist = light[0]
    timeElapsed += (road_length - lights[-1][0])    

    return timeElapsed



if __name__ == '__main__':

    N, L = map(int,input().split(' '))

    lights = []
    for _ in range(N):
        lights.append( tuple(map(int,input().split(' '))) )
        
    print( solve(lights, L) )