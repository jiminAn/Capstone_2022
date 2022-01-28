import sys
from collections import defaultdict

input_file = sys.argv[1]
n = int(sys.argv[2])
terms = defaultdict(float)

with open(input_file, 'r') as f:
    for line in f.readlines():
        term, tfidf, _, _ = line.strip().split('\t')
        #print(term, tfidf)
        terms[term] = tfidf

sorted_terms = sorted(terms.items(),key=lambda x:x[1],reverse=True)
top_n_terms = sorted_terms[:n]

for term, tfidf in top_n_terms:
    print(term,tfidf,sep='\t')


