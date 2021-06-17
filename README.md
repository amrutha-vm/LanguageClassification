# LanguageClassification
Language Classificatiob between English and Dutch

##Author: Amrutha Varshini Mandalreddy

## HOW TO TRAIN THE SYSTEM:
We could train the system using Decision trees or Adaboost. The serialized object of our
training is stored in trained.pickle file.

**Python3 train.py `<examples>` `<hypothesisOut>` `<learning-type>`**

To train the system using decision trees, the learning type argument is “dt”, for Adaboost it is “ada” <br />
Python3 train.py train.dat train_dt.pickle dt Python3 train.py train.dat train_ada.pickle ada
  
## HOW TO PREDICT:
The serialized object is stored at our desired location, and we load the object from the file
and predict output for the required examples.The prediction is based on the type of object stored in the file i.e it is a decision tree, then
it predicts using the decision tree. If it is an ensemble of hypotheses, then it employs AdaBoost prediction.

**Python predict.py `<hypothesis>` `<file>`**

python3 predict.py train_dt.pickle test1.txt <br />
python3 predict.py train_ada.pickle test1.txt

## HOW TO CHECK ERROR:
errorRate.py file can be used to calculate the error rates for different maxDepths of decision trees.

**Usage: python3 errorRate.py​ ​`<examples> <learning-type> <max-tree-depth> <test-data-file> <expected-output-file>`**

python3 errorRate.py​ ​train.dat dt 8 test1.txt expectedOP1.txt python3 errorRate.py​ ​train.dat ada 0 test1.txt expectedOP1.txt <br />
To execute without any maxDepth put the max-tree-depth to 0 Similarly for test2.txt and expectedOP2.txt <br />
python3 errorRate.py​ ​train.dat dt 0 test2.txt expectedOP2.txt python3 errorRate.py​ ​train.dat ada 0 test2.txt expectedOP2.txt <br />
