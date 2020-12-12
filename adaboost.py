__author__ = "Amrutha Varshini Mandalreddy"
__email__ = "am5739@rit.edu"

import math

from Node import node

ensemble = [0]
examples_classification = []
stumps_count=11


def createDecisionStumps(attribute, examples):
    # en considered positive, nl negative
    attribute_node = node(None, attribute, None, None)
    pT = 0;
    nT = 0;
    pF = 0;
    nF = 0;
    for example in examples:
        if example[attribute.attributeId]:
            if example[0] == "en":
                pT = pT + 1;
            else:
                nT = nT + 1
        else:
            if example[0] == "en":
                pF = pF + 1;
            else:
                nF = nF + 1
    # if pT/(pT+nT)>=0.5:
    if pT > nT:
        attribute_node.addChild(None, None,None, "True", "en")
    else:
        attribute_node.addChild(None, None,None,  "True", "nl")
    # if pF/(pF+nF)>=0.5:
    if pF > nF:
        attribute_node.addChild(None, None, None, "False", "en")
    else:
        attribute_node.addChild(None, None,None, "False", "nl")
    ensemble.append(attribute_node)
    #print(attribute_node)


def getDecision(node, value):
    children = node.children
    for child in children:
        if child.parent_value == value:
            return child.decision


def normalizeWeights(example_weights):
    sum = 0;
    for ex in example_weights:
        sum = sum + ex
    for i in range(0, len(example_weights)):
        example_weights[i] = example_weights[i] / sum
    return example_weights


def adaboostTraining(examples, example_weights, attributes):
    for i in range(1, stumps_count+1):
        createDecisionStumps(attributes[i], examples)

    for i in range(1, stumps_count+1):
        decisionIfTrue = getDecision(ensemble[i], "True")
        decisionIfFalse = getDecision(ensemble[i], "False")
        correctlyClassified = 0;
        notCorrectlyClassified = 0
        correctlyClassifiedIndices = []
        notCorrectlyClassifiedIndices = []
        j = 0;
        tempError = 0;
        for example in examples:
            if (example[i] == True and example[0] == decisionIfTrue) or \
                    (example[i] == False and example[0] == decisionIfFalse):
                correctlyClassified = correctlyClassified + 1
                correctlyClassifiedIndices.append(j)
            else:
                tempError = tempError + example_weights[j]
                notCorrectlyClassifiedIndices.append(j)
                notCorrectlyClassified = notCorrectlyClassified + 1
            j = j + 1
        error = tempError
        t = 1 - error
        w = error / t
        # Multiple w with weights of incorrectly classified examples
        if w <= 1:
            for k in correctlyClassifiedIndices:
                example_weights[k] = example_weights[k] * w
        else:
            for k in notCorrectlyClassifiedIndices:
                example_weights[k] = example_weights[k]* w

        example_weights = normalizeWeights(example_weights)
        attributes[i].updateWeight(math.log((t / error), 10))
    # print("Attribute weights ", attributes)
    return ensemble
