# predict 수행 방법

1. model_download.py 실행 -> koelectra-wellness-text-classification.pth가 폴더 내에 생성
2. koelectra.py 실행
3. module.py 실행
4. predict.py 혹은 category_indexing_predict.py 실행


## Test 결과

### 카테고리 통합 방법
A. category_indexing_predict.py
  + 배경/생활/여행/파리 --> 배경/생활 
  + 앞에 2개의 카테고리만 같으면 같은 카테고리로 인정

### 모든 카테고리 기준 (predict.py 실행)
1. Accuracy: 0.58
2. Recall: 0.48
3. Precision: 0.45
4. F1: 0.46

### 174개의 카테고리 기준 (category_indexing_predict.py 실행)
1. Accuracy: 0.64
2. Recall: 0.47
3. precision: 0.45
4. F1: 0.45
