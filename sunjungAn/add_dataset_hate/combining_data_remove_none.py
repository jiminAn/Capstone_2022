
wellness_data = "cur_data\index_category.txt" #이 곳에 question_index로 되어있는 파일 경로를 넣어줌
hate_data = "cur_data/dataset.comment_hate.result2" #이 곳에 지민언니가 올려준 dataset.comment_hate.result2 파일 경로를 넣어줌

save_file = "cur_data/combining_data_remove_none.txt" #이 곳에 저장할 파일 경로 지정

#여는 파일 읽는 부분
X = []
y = []
with open(wellness_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        list = line.strip().split('\t')
        X.append(list[0])
        y.append(list[1])

f.close()

temp = int(y[len(y)-1])

with open(hate_data, 'r', encoding = "utf-8") as f:
    for line in f.readlines():
        list = line.strip().split('\t')
        if(int(list[1]) != 0):
            X.append(list[0])
            y.append(str(temp+int(list[1])))



#저장하는 부분
f = open(save_file,'w', newline='',encoding='utf-8')

for xi,yi in zip(X,y):
    s = xi+"\t"+yi+"\n"
    f.write(s)
f.close()
