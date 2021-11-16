from model.load_kobert import DialogKoBERT

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

test ='./data/test_data.txt'
t_d = open(test,'r', encoding='UTF8')
test_lines = t_d.readlines()
test_data = []
target = []
predict=[]
for line_num, line_data in enumerate(test_lines):
    data = line_data.split('    ')
    a = data[1][:-1]
    test_data.append(data[0][:-1])
    target.append(a.lstrip())

kobert = DialogKoBERT()
for i, data in enumerate(test_lines):
    predict.append(kobert.predict(test_data[i]))
    # print(test_data[i])
    print(i, end=' ')
print("\n")
# for i, data in enumerate(target):
#     if data == predict[i]:
#         print(i, 'yes', data, predict[i])
#     else:
#         print(i, data, predict[i])

print('Accuracy: %.2f' % accuracy_score(target, predict))
print('Recall: %.2f' % recall_score(target, predict, average='macro'))
print('Precision: %.2f' % precision_score(target, predict, average='macro'))
print('F1: %.2f' % f1_score(target, predict, average='macro'))



