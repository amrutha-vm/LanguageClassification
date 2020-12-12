__author__ = "Amrutha Varshini Mandalreddy"
__email__ = "am5739@rit.edu"

import pickle
import sys

import Entropy
from Entropy import *
from LoadData import *
from adaboost import *
from Node import node

maxDepth = 20
stumps_count = 11

def train(examples_file, hypothesisOut_file, learning_type, maxTreeDepth):
    global maxDepth
    createAttributes()
    if learning_type == "dt":
        (examples, examples_weights) = load_examples(examples_file, "train", "dt")
        if len(examples) == 0:
            print("No Data to Train")
        else:
            root = node(examples, None, 1, None, None)
            if maxTreeDepth is not None:
                maxDepth = maxTreeDepth
            Entropy.maxDepth = maxDepth
            create_decision_tree(examples, attributes, None, None, root, 1)
            pickle_out = open(hypothesisOut_file, "wb")
            pickle.dump(root, pickle_out)
            pickle_out.close()
            # print(root)
    elif learning_type == "ada":
        (examples, examples_weights) = load_examples(examples_file, "train", "ada")
        if len(examples) == 0:
            print("No Data to Train")
        else:
            ensemble = adaboostTraining(examples, examples_weights, attributes)
            pickle_out = open(hypothesisOut_file, "wb")
            pickle.dump(ensemble, pickle_out)
            pickle_out.close()
    else:
        print("Usage: train.py <examples> <hypothesisOut> <learning-type>")


def main():
    args = sys.argv
    if len(args) == 4:
        examples_file = args[1]
        hypothesisOut_file = args[2]
        learning_type = args[3]
        train(examples_file, hypothesisOut_file, learning_type, None)
    else:
        print("Usage: train.py <examples> <hypothesisOut> <learning-type>")
        return


if __name__ == "__main__":
    main()
