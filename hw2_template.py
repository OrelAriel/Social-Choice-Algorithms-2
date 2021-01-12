import pandas as pd
import csv
from collections import defaultdict
import math
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt

# Make sure you are reading the data file either like this:
data = pd.read_csv('votes.csv', header=None)
# Or like this:
with open('votes.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        pass


def DTD_borda(votes):
    pass


def DTD_Copeland(votes):
    pass


def PTD_borda(votes):
    pass


def PTD_Copeland(votes):
    pass


def UW_borda(votes):
    pass


def UW_Copeland(votes):
    pass


def your_algorithm(votes, additional_parameters):
    pass


with open("estimations.csv", 'w', newline='') as file:
    wr = csv.writer(file)
    wr.writerow(DTD_borda())
    wr.writerow(DTD_Copeland())
    wr.writerow(PTD_borda())
    wr.writerow(PTD_Copeland())
    wr.writerow(UW_borda())
    wr.writerow(UW_Copeland())
    wr.writerow(your_algorithm())  # If implemented
