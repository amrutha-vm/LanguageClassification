__author__ = "Amrutha Varshini Mandalreddy"
__email__ = "am5739@rit.edu"

import math

# Lets consider English as positive and Dutch as negative
from Node import node

maxDepth = 0;

def calculate_goal_entropy(data):
    if len(data) > 0:
        p = 0;
        n = 0;
        for i in range(0, data.__len__()):
            if data[i][0] == 'en':
                p = p + 1
            elif data[i][0] == 'nl':
                n = n + 1

        if len(data[0]) == 2:
            # If there is only one attribute left and there are multiple output values
            # then take the value which is repeated maximum number of times
            if p > n:
                return "en"
            else:
                return "nl"
        else:
            if p == 0:
                return "nl"
            elif n == 0:
                return "en"
            else:
                return entropy_boolean_random_variable(p / (p + n))
    else:
        return None


def entropy_boolean_random_variable(p):
    if p == 0 or p == 1:
        return 0
    else:
        return -((p * math.log(p, 2)) + ((1 - p) * math.log(1 - p, 2)))


def calculate_InformationGain(goal_entropy, data, index):
    attribute_values = {};
    for i in range(0, data.__len__()):

        if attribute_values.__contains__(data[i][index]):
            if data[i][0] == 'en':
                attribute_values[data[i][index]][0] = attribute_values[data[i][index]][0] + 1;
            else:
                attribute_values[data[i][index]][1] = attribute_values[data[i][index]][1] + 1;
        else:
            attribute_values[data[i][index]] = [0, 0]
            if data[i][0] == 'en':
                attribute_values[data[i][index]][0] = 1;
            else:
                attribute_values[data[i][index]][1] = 1;
    remainder = 0;
    for values_p_n in attribute_values.values():
        remainder = remainder + ((values_p_n[0] + values_p_n[1]) / len(data)) * entropy_boolean_random_variable(
            values_p_n[0] / (values_p_n[0] + values_p_n[1]))
    return round(goal_entropy - remainder, 3);


# If the tree depth is more than the max depth, we are stopping the tree to grow further
# and giving out the results
def makeADecision(cuurentNode, parentDepth):
    p=0;
    n=0;
    for example in cuurentNode.data:
            if example[0] == "en":
                p = p + 1;
            else:
                n = n + 1
    # if pT/(pT+nT)>=0.5:
    if p > n:
        cuurentNode.addDecision("en")
    else:
        cuurentNode.addDecision("nl")


def create_decision_tree(data, attributes, parent, parentValue, deicion_tree, parentDepth):
    global maxDepth
    if maxDepth!= 0 and parentDepth >= maxDepth:
        makeADecision(deicion_tree, parentDepth)
        return deicion_tree
    currentDepth = parentDepth + 1;
    if len(data) == 0:
        pass
        # print("END")
    elif len(attributes) == 0:
        pass
        # print("END")
    else:
        goal_entropy = calculate_goal_entropy(data)

        if goal_entropy == "en":
            deicion_tree.addDecision("en")
            #deicion_tree.addDecision(data, parent, currentDepth, parentValue, "en")
            return deicion_tree
            # print("DONE", "en", " parent ", parent, " parentValue ", parentValue)
        elif goal_entropy == "nl":
            deicion_tree.addDecision("nl")
            # print("DONE", "B", " parent ", parent, " parentValue ", parentValue)
            #deicion_tree.addDecision(data, parent, currentDepth, parentValue, "nl")
            return deicion_tree
        else:
            informationGains = []
            informationGains.append(-1)
            max_entropy = -1
            max_entropy_Index = 0;
            for i in range(1, len(attributes)):
                temp = calculate_InformationGain(goal_entropy, data, i)
                informationGains.append(temp)
                if (temp > max_entropy):
                    max_entropy = temp
                    max_entropy_Index = i;

            # split data based on the value
            data1 = []
            data2 = []
            attributes_new = attributes.copy()
            for item in data:
                if item[max_entropy_Index] == True:
                    item.pop(max_entropy_Index)
                    data1.append(item)
                else:
                    item.pop(max_entropy_Index)
                    data2.append(item)
            parent_attribute = attributes_new.pop(max_entropy_Index)
            deicion_tree.addAttribute(parent_attribute)
            child1 = deicion_tree.addChild(data1, None, currentDepth, "True")
            child2 = deicion_tree.addChild(data2, None, currentDepth, "False")
            create_decision_tree(data1, attributes_new, parent, "True", child1, currentDepth)
            create_decision_tree(data2, attributes_new, parent, "False", child2, currentDepth)
            return deicion_tree
