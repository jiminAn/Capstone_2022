from konlpy.tag import Mecab
import sys

mecab = Mecab()
input_file = sys.argv[1]
tokenized = []

with open(input_file, 'r') as f:
	for line in f.readlines():
		q, idx = line.split('\t')
		tokenized.append(mecab.morphs(q.strip()))


for morphs in tokenized:
	print(' '.join(morphs), end ='\t')
	print(idx, end ='')
		
		
