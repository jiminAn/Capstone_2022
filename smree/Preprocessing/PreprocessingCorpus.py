import os
import sys
import re

allTrash = ''
    
def filtering(str):
    filt = re.compile('[^ 가-힣A-Za-z0-9\?\.!~%,\'+]')
    result = filt.sub('', str)
    trash = ''.join(filt.findall(str))
    global allTrash
    allTrash += trash
    return result, len(trash)

if __name__ == '__main__':
    input_file = os.path.join('data', 'Corpus.tsv')
    
    with open(input_file, 'r') as f:
        is_first = True
        for line in f.readlines():
            if is_first:
                is_first = False
                continue
            line = line.strip().split('\t')
            q, qb = filtering(line[1])
            a, ab = filtering(line[2])
            print(filtering(line[1])[0], filtering(line[2])[0], sep = '\t')
    #print(allTrash)