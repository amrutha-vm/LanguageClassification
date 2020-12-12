__author__ = "Amrutha Varshini Mandalreddy"
__email__ = "am5739@rit.edu"

import sys

from train import train
from Predict import predictFromData

def trainAndrunPredictionMode_dt(examples_file,hypothesis_out_file, learning_type, maxTreeDepth, testDataFile):
    train(examples_file, hypothesis_out_file, learning_type, maxTreeDepth)
    result = predictFromData(hypothesis_out_file, testDataFile)
    return result

def trainAndrunPredictionMode_ada(examples_file,hypothesis_out_file, learning_type, testDataFile):
    train(examples_file, hypothesis_out_file, learning_type, None)
    result = predictFromData(hypothesis_out_file, testDataFile)
    return result

def errorRate():
    args = sys.argv
    if len(args) == 6:
        examples_file = args[1]
        learning_type = args[2]
        maxTreeDepth = (int)(args[3])
        if maxTreeDepth==0:
            maxTreeDepth = None
        testDataFile = args[4]
        expectedOutputFile = args[5]
        expected = open(expectedOutputFile, 'r').readlines()
        if learning_type=="dt":
            ActualOutPUT = trainAndrunPredictionMode_dt(examples_file, "trainForErrorRate.pickle", learning_type,
                                                    maxTreeDepth, testDataFile)
        elif learning_type=="ada":
            ActualOutPUT = trainAndrunPredictionMode_ada(examples_file, "trainForErrorRate.pickle", learning_type,
                                                         testDataFile)

    else:
        ActualOutPUT = open("actualOutput1.txt")
        expected = open("expected1.txt", 'r').readlines()
    incorrectCount = 0
    totalCount=0
    for i in range(0, len(expected)):
        totalCount = totalCount+1
        if expected[i].rstrip() != ActualOutPUT[i].rstrip():
            incorrectCount = incorrectCount + 1
            print("LINE: ", (str)(i + 1), " EXPECTED: ", expected[i], " ACTUAL: ", ActualOutPUT[i])
    print("TOTAL INCORRECT: ", (str)(incorrectCount))
    print("Error Rate: " ,(incorrectCount*100/totalCount),"%")



errorRate()
