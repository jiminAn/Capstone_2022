import sys
input_file = sys.argv[1]

with open(input_file, 'r') as f:
	for line in f.readlines():
		q, a = "", ""
		if line[0] == 'S':
			head, txt = line.split('\t')
			print('Q\t',txt.strip())
			q_flag = True
		elif q_flag:
			txt = line.strip()
			print('A\t',txt.strip())
			q_flag = False

