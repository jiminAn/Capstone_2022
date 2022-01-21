import pandas as pd
import sys
import pprint as pp
from collections import defaultdict

input_file = sys.argv[1] # target file

with open(input_file, 'r') as f:
    for line in f.readlines():
        comment, hate_bool = line.strip().split('\t')
        print(hate_bool, comment, sep = '\t')
