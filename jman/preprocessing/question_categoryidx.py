import pandas as pd
import sys
import pprint as pp
from collections import defaultdict

input_file1 = sys.argv[1] # target file
input_file2 = sys.argv[2] # category-index information

category_dic = defaultdict(int)
with open(input_file2, 'r') as f:
    for line in f.readlines():
        category, idx = line.strip().split('\t')
        category_dic[category] = idx

#print(category_dic)

with open(input_file1, 'r') as f:
    for line in f.readlines():
        comment, hate_bool = line.strip().split('\t')
        print(comment, category_dic[hate_bool], sep='\t')
