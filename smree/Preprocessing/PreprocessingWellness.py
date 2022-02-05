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
    input_file = os.path.join('data', 'Wellness.tsv')
    
    phase = 1
    can_phase_end = False
    que_buff = []
    ans_buff = []
    d = []
    
    with open(input_file, 'r') as f:
        is_first = True
        for line in f.readlines():
            if is_first:
                is_first = False
                continue
            
            line = line.strip().split('\t')
            if can_phase_end and len(line) == 3:
                phase += 1
                # clear buff
                for q in que_buff:
                    for a in ans_buff:
                        d.append((q, a))
                can_phase_end = False
                que_buff.clear()
                ans_buff.clear()
            q = filtering(line[1])[0]
            
            que_buff.append(q)
            if len(line) == 2:
                can_phase_end = True
            elif len(line) == 3:
                a = filtering(line[2])[0]
                ans_buff.append(a)
            
        for (q, a) in d:
            print(q, a, end = '\n', sep = '\t')
            
        #print(allTrash)
            