from numpy.lib.function_base import average
from sklearn import metrics
import module
import sklearn.metrics as metrics

TARGET_FILE = "./data/wellness_dialog_category.txt"
TEST_FILE = "./data/test_data.txt"



target_file = open(TARGET_FILE, 'r', encoding = 'utf-8')
category = [0]
category_list = []
#=========================================================


#==========================================================
pre_line = "구분"
i = 0
while True:
    line = target_file.readline()
    if not line:
        break
    categories = line.split("\t")
    category_list.append(categories[0])
    new_category = categories[0].split('/')
    if len(new_category) == 1:
        continue
    categories = new_category[0]+'/'+new_category[1]
    if(categories == pre_line):
        category.append(i)
    else:
        i = i+1
        category.append(i)
        pre_line = categories
    print(categories, i)
    


#========================================================
test_file = open(TEST_FILE, 'r', encoding = "utf-8")
X = []
y = []

while True:
    line = test_file.readline()
    if not line:
        break
    datas = line.split("    ")
    X.append(datas[0])
    y_ = category_list.index(datas[1].strip())
    y.append(category[y_])

print(y)

model = module.DialogElectra()

accuracy = 0
y_hat = []
for xi, yi in zip(X, y):
    sentence=xi
    y_i = model.predict(sentence)
    y_hat.append(category[y_i])

print('Accuracy: %.2f' % metrics.accuracy_score(y, y_hat))
print('Recall: %.2f' % metrics.recall_score(y, y_hat, average="macro"))
print('Precision: %.2f' % metrics.precision_score(y, y_hat, average="macro"))
print('F1: %.2f' % metrics.f1_score(y, y_hat, average="macro"))
