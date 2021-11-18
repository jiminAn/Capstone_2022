from numpy.lib.function_base import average
from sklearn import metrics
from model.load_kobert import DialogKoBERT
import sklearn.metrics as metrics

TEST_FILE = "./data/test_data.txt"
TARGET_FILE = "./data/category.txt"

categories = []
with open(TARGET_FILE, 'r') as f:
	for line in f.readlines():
		category, _ = line.split('\t')
		categories.append(category)

X = []
y = []

with open(TEST_FILE, 'r') as f:
	for line in f.readlines():
		convers, category = line.split('\t')
		X.append(convers)
		y.append(category.strip())

print("Size of test set: ", len(y))

model = DialogKoBERT()

accuracy = 0
y_hat = []
print("qustion","answer","predict",sep='\t')
for xi, yi in zip(X, y):
	predict = model.predict(xi)
	print(xi,yi,predict,sep='\t')
	y_hat.append(predict)

print('Accuracy: %.2f' % metrics.accuracy_score(y, y_hat))
print('Recall: %.2f' % metrics.recall_score(y, y_hat, average="micro"))
print('Precision: %.2f' % metrics.precision_score(y, y_hat, average="micro"))
print('F1: %.2f' % metrics.f1_score(y, y_hat, average="micro"))

