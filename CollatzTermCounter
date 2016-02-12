__author__ = 'Cyph3r (Matthew Gakowski)'
__copyright__ = "Copyright 2016, Collatz-Sequence-Term-Analyzer"
__credits__ = ["Matthew Gakowski"]
__license__ = "GPL v3.0"
__version__ = "1.0"
__maintainer__ = "Matthew Gakowski"
__email__ = "mgakowski@gmail.com"
__status__ = "Production"

N = 10
X = N
stepCount = 1
highestS = 0
highestN = 0
g = 0
 
f = str(input("Please name new file: "))
g = int(input("Limit to calculate to? "))
text_file0 = open(f+".txt", "w")
 
while N != g+1:
    if X == 1:
        text_file0.write(str(N)+":"+str(stepCount)+"\n")
        print(str(N)+" : "+str(stepCount))
        if stepCount > highestS:
            print("* "+str(N)+" : "+str(stepCount))
            highestS = stepCount
            highestN = N
        stepCount = 1
        N += 1
        X = N
    else:
        if X % 2 == 0:
            X /= 2
            stepCount += 1
        else:
            X = X * 3 + 1
            stepCount += 1
else:
    print("Largest Collatz sequence with most terms = "+str(highestN)+" with "+str(highestS)+" terms!")
    text_file0.close()
