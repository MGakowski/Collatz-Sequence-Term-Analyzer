N = 1
X = N
stepCount = 0
highestS = 0
highestN = 0
g = 0
number = 1


while True:
    if X == 1:
        if stepCount > highestS:
            print("#" + str(number) +" biggest Collatz is " + str(N) + " after " + str(stepCount) + " steps.")
            number += 1
            highestS = stepCount
            highestN = N
        stepCount = 0
        N += 1
        X = N
    else:
        if X % 2 == 0:
            X /= 2
            stepCount += 1
        else:
            X = X * 3 + 1
            stepCount += 1
