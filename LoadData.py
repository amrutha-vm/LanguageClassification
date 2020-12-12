__author__ = "Amrutha Varshini Mandalreddy"
__email__ = "am5739@rit.edu"

from Node import *

ruleCount = 10
attributes = [];


def createAttributes():
    attributes.append(attribute(0, "Language"))
    attributes.append(attribute(1, "Contains the? "))
    attributes.append(attribute(2, "Contains de? "))
    attributes.append(attribute(3, "Contains het? "))
    attributes.append(attribute(4, "Contains  a ? "))
    attributes.append(attribute(5, "Contains  an? "))
    attributes.append(attribute(6, "Contains  een ? "))
    attributes.append(attribute(7, "Contains ij? "))
    attributes.append(attribute(8, "Contains  aa ? "))
    attributes.append(attribute(9, "Contains  en ? "))
    attributes.append(attribute(10, "Contains  oo ? "))
    attributes.append(attribute(11, "Contains  oe ? "))


def convert_examples_hypothesis(examples, learningType):
    if len(examples)==0:
        return [], None
    rules = []
    s = ""
    if learningType == "ada":
        examples_weights = []
        temp = 1 / len(examples)
    else:
        examples_weights = None
    for example in examples:
        rule = []
        if learningType == "ada":
            examples_weights.append(temp)
        s = s + example[0] + "|"
        rule.append(example[0])
        # 1.  sentence contains word " the "
        if example[1].__contains__(" the "):
            rule.append(True)
        else:
            rule.append(False)

        # 2.  sentence contains word " de "
        if example[1].__contains__(" de "):
            rule.append(True)
        else:
            rule.append(False)

        # 3.  sentence contains word " het "
        if example[1].__contains__(" het "):
            rule.append(True)
        else:
            rule.append(False)

        # 4.  sentence contains word " a "
        if example[1].__contains__(" a "):
            rule.append(True)
        else:
            rule.append(False)

        # 5.  sentence contains word " an "
        if example[1].__contains__(" an "):
            rule.append(True)
        else:
            rule.append(False)

        # 6.  sentence contains word "een"
        if example[1].__contains__("een"):
            rule.append(True)
        else:
            rule.append(False)

        # 7.  sentence contains words with  "ij"
        if example[1].__contains__("ij"):
            rule.append(True)
        else:
            rule.append(False)

        # 8.  sentence contains words with  "aa"
        if example[1].__contains__("aa"):
            rule.append(True)
        else:
            rule.append(False)

        # 9.  sentence contains word " en "
        if example[1].__contains__(" en "):
            rule.append(True)
        else:
            rule.append(False)
        rules.append(rule)

        # 10.sentence contains words with  "oo"
        if example[1].__contains__("oo"):
            rule.append(True)
        else:
            rule.append(False)

        # 11.sentence contains words with  "oe"
        if example[1].__contains__("oe"):
            rule.append(True)
        else:
            rule.append(False)

    return rules, examples_weights


def load_examples(filename, type, learningType):
    file = open(filename, 'r')
    examples = [];
    if type is None or type == "train":
        for line in file:
            if line != "\n":
                examples.append(line.rstrip().split("|"))
    elif type == "test":
        for line in file:
            if line!="\n":
                example = [" ", line.rstrip()]
                examples.append(example)
    return convert_examples_hypothesis(examples, learningType)



