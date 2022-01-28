import sys
import os
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

input_file = sys.argv[1]
corpus = []

with open(input_file, 'r') as f:
    for line in f.readlines():
        line = line.strip()
        q, idx = line.split('\t')
        corpus.append(q)

#print(corpus)

vect = CountVectorizer()
document_term_matrix = vect.fit_transform(corpus) # matrix for document-term
#print(document_term_matrix)


tf = pd.DataFrame(document_term_matrix.toarray(), columns=vect.get_feature_names_out())
D = len(tf)
df = tf.astype(bool).sum(axis=0)
idf = np.log((D+1) / (df+1)) + 1

# TF-IDF (Term Frequency-Inverse Document Frequency)
tfidf = tf * idf
tfidf = tfidf / np.linalg.norm(tfidf, axis=1, keepdims=True)

sums = []
N = len(corpus)
print('term','tf-idf','tf','idf',sep='\t')
for col, item in tfidf.iteritems():
    print(col, tfidf[col].sum()/N,tf[col].sum(),idf[col].sum(),sep='\t')
