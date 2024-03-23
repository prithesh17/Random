import pandas as pd
import math
import numpy as np

class Node:
    def __init__(self):
        self.children = []  # List to hold child nodes
        self.value = ""     # Attribute value for current node
        self.isLeaf = False # Flag to indicate if the node is a leaf
        self.pred = ""      # Prediction if the node is a leaf

# Function to calculate entropy
def entropy(examples):
    pos = 0.0  # Number of positive examples
    neg = 0.0  # Number of negative examples

    # Count positive and negative examples
    for _, row in examples.iterrows():
        if row["play"] == "Yes":
            pos += 1
        else:
            neg += 1
    
    # Calculate entropy
    if pos == 0.0 or neg == 0.0:
        return 0.0
    else:
        p = pos / (pos + neg)  # Probability of positive examples
        n = neg / (pos + neg)  # Probability of negative examples
        return -(p * math.log(p, 2) + n * math.log(n, 2))  # Entropy calculation

# Function to calculate information gain for an attribute
def info_gain(examples, feature):
    uniq = np.unique(examples[feature])
    gain = entropy(examples)           # Entropy before splitting
    
    # Calculate information gain after splitting
    for u in uniq:
        subdata = examples[examples[feature] == u]
        sub_e = entropy(subdata)
        gain -= (len(subdata) / len(examples)) * sub_e
    
    return gain

# ID3 algorithm for decision tree construction
def ID3(examples, features):
    root = Node()          # Create a root node
    max_gain = 0           # Maximum information gain
    max_feat = ""          # Attribute with maximum gain
    
    # Find attribute with maximum information gain
    for feature in features:
        gain = info_gain(examples, feature)
        if gain > max_gain:
            max_gain = gain
            max_feat = feature
    
    root.value = max_feat  # Set the attribute with max gain for the root
    uniq = np.unique(examples[max_feat])  # Unique values of the selected attribute
    # Recursively create child nodes
    for u in uniq:
        subdata = examples[examples[max_feat] == u]
        if entropy(subdata) == 0.0:  # If entropy is 0, create a leaf node
            newNode = Node()
            newNode.isLeaf = True
            newNode.value = u
            newNode.pred = np.unique(subdata["play"])
            root.children.append(newNode)
        else:  # Otherwise, create a non-leaf node
            dummyNode = Node()
            dummyNode.value = u
            new_attrs = features.copy()
            new_attrs.remove(max_feat)  # Remove current attribute from list
            child = ID3(subdata, new_attrs)  # Recursively create child node
            dummyNode.children.append(child)
            root.children.append(dummyNode)
    
    return root

# Function to print the decision tree
def printTree(root, depth=0):
    for i in range(depth):
        print("\t", end="")
    print(root.value, end="")
    if root.isLeaf:
        print(" -> ", root.pred)
    print()
    for child in root.children:
        printTree(child, depth + 1)

# Function to classify a new example using the decision tree
def classify(root, new):
    for child in root.children:
        if child.value == new[root.value]:
            if child.isLeaf:  # If leaf node, print prediction
                print("Predicted Label for new example", new, " is:", child.pred)
                return
            else:  # Otherwise, traverse further
                classify(child.children[0], new)

# Load dataset
data = pd.read_csv("tennis.csv")

# Extract features (attributes)
features = list(data.columns)
features.remove("play")  # Remove target attribute
features.remove("day")   # Remove irrelevant attribute

# Build decision tree using ID3 algorithm
root = ID3(data, features)

# Print decision tree
print("Decision Tree is:")
printTree(root)
print("------------------")

# Classify new example
new_example = {"outlook": "Sunny", "temp": "Hot", "humidity": "High", "windy": "Weak"}
classify(root, new_example)
