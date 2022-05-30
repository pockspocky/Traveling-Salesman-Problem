from random import choice
import itertools as it
import traceback
import sys
import string
import time


# Design Requirements Below:
# Eliminate Most paths
# Optimize to as low as possible

def distanceGenerator(numOfDestinations=5):
    def numOfPathsGeneration():
        numOfPathsToEachDestinations = 0
        for destination in range(1, numOfDestinations + 1):
            numOfPathsToEachDestinations += destination
        return numOfPathsToEachDestinations

    def randomDistanceGeneration():
        choices = [temp for temp in range(1, numOfPathsGeneration() + 1)]
        for temp in range(numOfPathsGeneration()):
            temporaryStorage = choice(choices)
            choices.remove(temporaryStorage)
            yield temporaryStorage

    return randomDistanceGeneration()


def possiblePathsGeneration(numOfPoints=5):
    flag = False
    alphabet = string.ascii_uppercase
    accumulator = 0
    terminateNum = 0
    flag2 = 0
    numOfPoints = numOfPoints

    if numOfPoints > 26:  # To see if it exceeds the alphabet

        letters = list(alphabet)  # filling in the list with existing alphabet
        for repeater in range(2, ((numOfPoints - 1) // 26) + 2):  # How many times the letter will repeat itself (You will see in the output what I mean)

            for y in alphabet[:26]:  # repeats over the alphabet

                if flag2 == 1:  # Prevents another whole alphabet generating
                    break

                if numOfPoints % 26 > 0 and (numOfPoints - 26) // 26 < 1:  # To see if it has any spare letters that does not form a full alphabet
                    terminateNum = numOfPoints % 26  # calculates how many spare letters are left out and sets it as a termination number for later
                    flag = True  # Sets a flag which makes one of the if statements false which allows execution of later programs

                else:
                    terminateNum = (numOfPoints - 26) // 26  # Getting the times that the alphabet has to iterate through

                if flag is True and numOfPoints % 26 > 0 & (numOfPoints - 26) // 26 < 1:  # To see if we have a whole alphabet
                    break

                if accumulator >= terminateNum:  # Determines when to leave the loop
                    break

                letters.append(y * repeater)  # Outputs point
            accumulator += 1
            if flag is not True & accumulator != terminateNum | accumulator <= terminateNum:  # Determines if we have more whole alphabets
                continue

            terminateNum = numOfPoints % 26  # Resets number of letters to generate
            for y in alphabet[:terminateNum]:  # outputs the spares
                flag2 += 1
                if flag2 == 1 and not (numOfPoints < 52):  # prevents generation of extra letters
                    break
                letters.append(y * repeater)

    else:
        letters = list(alphabet[:numOfPoints])
    for combo in it.combinations(letters, 2):
        yield combo
    return letters


def allPathsDistanceAssignment(distances, allPaths):
    pathDistanceReference = {path: distance for (path, distance) in zip(allPaths, distances)}
    return pathDistanceReference


def routeGen(pointCollection):
    points = [str(x) for x in pointCollection[1:]]
    routeCollection = []
    for route in it.permutations(points):
        x = " ".join(route)
        tempCheck = f"{pointCollection[0]} {x} {pointCollection[0]}".split()
        list(tempCheck)
        for x in range(2):
            if tempCheck not in routeCollection and tempCheck[::-1] not in routeCollection:
                routeCollection.append(tempCheck)
            tempCheck = tempCheck[::-1]
    return routeCollection


def bruteForceAlgorithm(routes, distances):
    count1 = 0
    count2 = 2
    total = 0
    routeDistance = {}
    for route in routes:
        for times in range(len(route) - 1):
            temp = route[count1: count2]
            temp.sort()
            temp = tuple(temp)
            total += distances[temp]
            count1 += 1
            count2 += 1
        # print(f"{' '.join(route)} \t \t \t {total}")
        routeDistance |= {' '.join(route): total}
        total = 0
        count1 = 0
        count2 = 2
    return routeDistance

def main():
    pointsNeeded = 5
    gen = possiblePathsGeneration(pointsNeeded)
    points = []

    try:
        while True:
            next(gen)
    except StopIteration as e:
        points = e.value

    route = routeGen(points)
    pathDistance = allPathsDistanceAssignment(distanceGenerator(pointsNeeded), possiblePathsGeneration(pointsNeeded))  # Distance assignment in one line
    x = bruteForceAlgorithm(route, pathDistance)
    sortedItems = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    print({k: v for k, v in sorted(pathDistance.items(), key=lambda item: item[1])})
    for sort_key, sort_value in sortedItems.items():
        print(f"{sort_key} = {sort_value}")

if __name__ == '__main__':
    main()


