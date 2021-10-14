#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    steps = 0;
    maxAlt = 0;
    minAlt = 0;
    for i in range(len(path)):
        if(path[i]=="U"):
            steps+=1
            maxAlt = steps if steps>maxAlt else maxAlt;
        else:
            steps-=1;
            minAlt = steps if steps<minAlt else minAlt;
    n_h_travel = 0
    n_v_travel = 0
    steps = 0
    equalizer = True;
    prevTravel = ""
    for i in range(len(path)):
        steps = steps+1 if path[i]=="U" else steps-1;
        if (i!=0):
            stepTravel = "Hill" if path[i-1]=="U" else "Valley"
        if(steps==maxAlt and (prevTravel=="" or prevTravel=="Valley" or (stepTravel=="Valley" and equalizer))):
            n_h_travel = n_h_travel+1
            prevTravel = "Hill"
            equalizer = False;
        elif(steps==minAlt and (prevTravel=="" or prevTravel=="Hill" or (stepTravel=="Hill" and equalizer))):
            n_v_travel= n_v_travel+1
            prevTravel = "Valley";
            equalizer = False;
        elif(steps==0):
            equalizer=True;
    return n_v_travel; 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
