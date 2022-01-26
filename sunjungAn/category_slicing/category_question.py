import pandas as pd
import csv
import sys
import pprint as pp
from collections import defaultdict

input_file = 'data.csv' # target file
output_file = 'category.csv'
X = []
y = []
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        list = line.strip().split('\t')
        X.append(list[1])
        label = list[0].split('/')
        if(len(label)>=3):
            list[0] = label[0]+"/"+label[1]
        y.append(list[0])

X.pop(0)
y.pop(0)

f = open('category_question.csv','w', newline='')
wr = csv.writer(f)
for xi,yi in zip(X,y):
    wr.writerow([yi, xi])
f.close()

category = []
idx = 0
prev = ""

f = open('category_index.csv','w', newline='')
wc = csv.writer(f)
for yi in y:
    if(prev != yi):
        wc.writerow([idx, yi])
        prev = yi
        idx = idx + 1
f.close()
