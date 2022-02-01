wellness_index_data = "cur_data/category_index.txt" #wellness index 데이터 파일 경로 지정
hate_index_data = "cur_data/hate_category_index.txt" #hate index 데이터 파일 경로 지정

save_index_file = "cur_data/combining_index_remove_none.txt" # 저장할 파일 경로 지정

#여는 파일 읽는 부분
X = []
y = []
with open(wellness_index_data, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        list = line.strip().split('\t')
        X.append(list[0])
        y.append(list[1])

f.close()

temp = int(y[len(y)-1])

with open(hate_index_data, 'r', encoding = "utf-8") as f:
    for line in f.readlines():
        list = line.strip().split('\t')
        if(int(list[1])!= 0):
            X.append(list[0])
            y.append(str(temp+int(list[1])))



#저장하는 부분
f = open(save_index_file,'w', newline='',encoding='utf-8')

for xi,yi in zip(X,y):
    s = xi+"\t"+yi+"\n"
    f.write(s)
f.close()
