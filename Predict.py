__author__ = "Amrutha Varshini Mandalreddy"
__email__ = "am5739@rit.edu"

import pickle
import sys
from LoadData import load_examples


def predictFromDT(rootNode, examples):
    decisions = []
    for example in examples:
        currentNode = rootNode
        done = False
        while (not done):
            children = currentNode.children
            for child in children:
                if str(example[currentNode.attribute.attributeId]) == child.parent_value:
                    if child.decision is None:
                        currentNode = child
                    else:
                        done = True
                        decisions.append(child.decision)
                    break
    return decisions


def predictFromAda(ensemble, examples):
    result = []
    sums = []
    t = 0
    for ex in examples:
        t = t + 1
        sum = 0
        for i in range(1, len(ensemble) - 1):
            current = ensemble[i]
            res = current.getResult(str(ex[current.attribute.attributeId]))
            if res == "en":
                temp = 1
            else:
                temp = -1

            sum = sum + (current.attribute.weight * temp)
        sums.append(sum)
        if t == 25:
            te = 0
            pass
        if sum >= 0.7:
            result.append("en")
        else:
            result.append("nl")
    # print(result)
    # print(sums)
    return result

def predictFromData(hypothesisFile, testFile):
    try:
        pickle_in = open(hypothesisFile, "rb")
    except:
        print("Trained model doesnot exists at location - ", hypothesisFile)
        return
    model = pickle.load(pickle_in)
    pickle_in.close()
    if isinstance(model, list):
        for i in range(1, len(model)):
            current = model[i]
            # print(current.attribute, "\n when True: ", current.getResult("True"), "\n when False:",
            #       current.getResult("False"))
        test_examples = load_examples(testFile, "test", "ada")[0]
        result = predictFromAda(model, test_examples)
    else:
        test_examples = load_examples(testFile, "test", "dt")[0]
        result = predictFromDT(model, test_examples)
    return result

def main():
    args = sys.argv
    if len(args) == 3:
        hypothesisFile = args[1]
        testFile = args[2]
    result = predictFromData(hypothesisFile, testFile)
    if result is not  None:
        for line in result:
            print(line)
        return result


if __name__ == '__main__':
    main()
