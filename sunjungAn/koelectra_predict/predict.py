from numpy.lib.function_base import average
from sklearn import metrics
import module
import sklearn.metrics as metrics

TEST_FILE = "./data/test_data.txt"
TARGET_FILE = "./data/wellness_dialog_category.txt"


file = open(TEST_FILE, 'r', encoding='utf-8')
target_file = open(TARGET_FILE, 'r', encoding='utf-8')
category = []

while True:
    line = target_file.readline()
    if not line:
        break
    categories = line.split("\t")
    category.append(categories[0])


X = []
y = []
while True:
    line = file.readline()
    if not line:
        break
    datas = line.split("    ")
    #print(datas[0])
    X.append(datas[0])
    y.append(category.index(datas[1].strip()))

print("test: ", len(y))

model = module.DialogElectra()

accuracy = 0
y_hat = []
for xi, yi in zip(X, y):
    print(yi)
    sentence=xi
    y_hat.append(model.predict(sentence))

print('Accuracy: %.2f' % metrics.accuracy_score(y, y_hat))
print('Recall: %.2f' % metrics.recall_score(y, y_hat, average="macro"))
print('Precision: %.2f' % metrics.precision_score(y, y_hat, average="macro"))
print('F1: %.2f' % metrics.f1_score(y, y_hat, average="macro"))

