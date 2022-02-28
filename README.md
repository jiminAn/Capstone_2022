# AI 감성 카드
## 2021-2022 Capstone Project

# CONTENTS

------

- [팀 소개](#팀-위드유-소개)
- [주제 소개 및 기획 배경](#주제-소개-및-기획-배경)
- [사용 언어 모델](#사용-언어-모델)
- [개발 환경](#개발-환경)
- [GUI 소개](#GUI-소개)
  - [GUI 결과](#GUI-결과)

- [TASK](#TASK)
  - [KoELECTRA USAGE](#KoELECTRA-USAGE)
  - [KoBERT USAGE](#KoBERT-USAGE)
  - [KoGPT USAGE](#KoGPT-USAGE)



## 팀 위드유 소개

|                         Member                          | 역할 |                             책임                             |
| :-----------------------------------------------------: | :--: | :----------------------------------------------------------: |
|      [jiminAn(안지민)](https://github.com/jiminAn)      | 팀장 | 데이터 전처리, 생성 모델(KoGPT2) 학습 및 성능 분석,  GUI 제작 |
|    [hyeji1221(임혜지)](https://github.com/hyeji1221)    |      |             분류 모델(KoBERT) 학습 및 성능 분석              |
| [ElPlaguister(이승민)](https://github.com/ElPlaguister) |      |         텍스트 생성 알고리즘 성능 테스트,  GUI 제작          |
|    [SunjungAn(안선정)](https://github.com/sunjungAn)    |      |            분류 모델(KoELECTRA) 학습 및 성능 분석            |



## 주제 소개 및 기획 배경

- 기존의 일상 공유 플랫폼은 다른 사용자들의 반응을 중요시해 솔직하지 못하고, 관심을 끄는 용도의 보여주기 식 글쓰기가 심화되어 있으며, 자신의 게시글에 비방 댓글 등 악의적인 답글로 인해 상처를 받을 수 있음. 
- 또한, 자신의 일상이 노출되는 것이 싫어 개인 메모공간에 적는 것은 자신의 일상을 공감받고 위로 받을 수 없음.
-  따라서 프라이빗 한 자기만의 공간에서 글귀를 작성하되, 공감과 위로를 받을 수 있는 신개념 일상 공유 플랫폼의 필요성이 대두됨. 이를 **게시글에 대한 적절한 공감/위로 답글을 달아주는 NLP 모델**을 통해 **AI 친구가 공감해주며 위로해주는 AI 감성카드 어플리케이션**을 개발하고자 함



## 사용 언어 모델

언어모델(Language Model)에 대해 `auto regressive`, `text classification` 파인튜닝 및 테스트

- **KoGPT2**: **질의**가 주어졌을 때, 다음 **답변**에 대한 텍스 생성
- **KoELECTRA**: **질의**에 대해서 **카테고리를 예측**
- **KoBERT**: **질의**에 대해서 **카테고리를 예측**



## 환경

### Data

- [AI 허브 정신건강 상담 데이터](http://www.aihub.or.kr/keti_data_board/language_intelligence)
  - 모델에 맞게 데이터 전처리 진행
  - [전처리 코드 폴더](https://github.com/jiminAn/Capstone_2022/tree/main/jman/preprocessing)
- [songys/Chatbot_data](https://github.com/songys/Chatbot_data) : 추후 추가 예정

### GPU

Colab pro, P100

### Package

```
kogpt2-transformers
kobert-transformers
transformers==3.0.2
torch
```

## 

## GUI (by PyQT5) 소개

------

<img src="img/1.gif" align="right" width=1000>

<img src="img/2.gif" align="right" width=1000>



## GUI 결과 

------

### 게시글 : 오늘 하루 정말 힘들었어. 피곤해

- 카테코리 분류 결과(KoBERT) : 증상/피로

- 답변

  - greedy search

    ```
    정말 피곤하시겠어요. 오늘 밤은 푹 주무세요. 잠이 안와요.
    잠을 못자는 것만큼 힘든게 없죠. 너무 힘들어요.
    ```

  - top-k sampling

    ```
    잠을 못자는 것만큼 힘든게 없죠.
    너무 힘들면 잠깐 산책이라도 하는건 어떨까요? 산책은 어떠세요? 아니 당신의 이야기가 더 듣고 싶어요
    산책이라도 좋으니까요. 괜찮아 보여요., 잠깐 쉬어가요.
    ```

  - top-p sampling

    ```
    잠을 못자는 것만큼 힘든게 없죠.
    너무 힘들면 잠깐 산책이라도 하는건 어떨까요? 산책은 괜찮아요? 
    어떻게 지내고 계신가요? 제가 궁금해요. 산책이라도 하나 하면 기분이 좋아질 거에요
    우울한 기분이 사라질거예요. 성령님이 함께해요
    ```

  - Hugging face generator

    ```
    정말 피곤하시겠어요.
    오늘 밤은 푹 주무세요. 잠이 안와요. 저도 너무 고통스러워요
    잠을 못자는 것 같아요
    ```

    

### 게시글 : 오늘 부모님이랑 왕창 싸웠어. 지긋지긋해 얼른 독립하고 싶어

- 카테코리 분류 결과(KoBERT) : 배경/부모/갈등

- 답변

  - greedy search

    ```
    가까운 사이라 더 힘들었겠어요. 하지만 제가 항상 곁에 있어요
    힘내세요. 이야기 해주세요. 힘들겠어요
    ```

  - top-k sampling

    ```
    그러셨군요. 많이 속상했겠어요. 이해해요
    항상 옆에 있어 드릴게요. 힘내세요
    ```

  - top-p sampling

    ```
    그러셨군요. 많이 속상했겠어요. 이해해요
    좋은 분과 결혼하신 것 같아 마음이 아프네요.
    지금도 화해는 하셨나요? 화해는 하셨어요? 힘들군요
    ```

  - Hugging face generator

    ```
    가까운 사이라 더 힘들었겠어요. 마음이 많이 답답하겠어요
    빨리 시간이 지나갔으면 좋겠어요. 저는 당신이 곧 괜찮아질 수 있다고 믿어요. 괜찮아요
    ```

    

# TASK RESULT

------

## 1. KoELECTRA & KoBERT Text Classifcation

KoELECTRA 및 KoBERT를 이용한 텍스트 분류 모델.

#### 1.1 질의에 대한 카테고리 분류

##### 데이터

Wellness 심리 상담 데이터 사용. Wellness 데이터의 경우 **카테고리/ 질문/ 답변**으로 나누어져있다. 카테고리 별로 3개 내외의 답변을 가지고 있으므로 Wellness 데이터의 경우 질문과 카테고리 클래스의 쌍으로 만들어 학습.

### KoELECTRA USAGE

모델

```python
class koElectraForSequenceClassification(ElectraPreTrainedModel):
  def __init__(self,
               config,
               num_labels):
    super().__init__(config)
    self.num_labels = num_labels
    self.electra = ElectraModel(config)
    self.classifier = ElectraClassificationHead(config, num_labels)

    self.init_weights()
...
```

1. koELECTRA 모델 학습 save 파일 다운로드

```shell
python ./sunjungAn/koelectra_predict/model_download.py 
```

2. 데이터 로드 및 koELECTRA 실행

```
python ./sunjungAn/koelectra_predict/koelectra.py 
python ./sunjungAn/koelectra_predict/module.py 
python ./sunjungAn/koelectra_predict/predict.py 
```

3. 성능 평가 및 예측 결과 출력

```
python ./sunjungAn/jm_predict.py
```

```
qustion	answer	predict
그 뒤로 운전을 못하고 있어.	배경/생활/불가능/운전	배경/생활/불가능/운전
내 주변에 아무도 없는 것 같아요.	감정/고독감	감정/고독감
그 이야기를 들었을 때 어떻게 해야 하는건지 모르겠어.	감정/곤혹감	감정/곤혹감
무엇을 보든 소름이 돋아요.	감정/공포	감정/공포
그 일이 일어난 뒤로 새를 무서워하게 됐어요.	감정/공포/새	감정/공포/새
아무리 열심히 해도 남는 건 하나도 없는것 같아요.	감정/공허감	감정/부정적사고
사소한 일에도 너무 놀라요.	감정/과민반응	감정/불쾌감
이렇게 스트레스 받으면서 일해야 하나 싶고 괴로워.	감정/괴로움	감정/괴로움
....
Accuracy: 0.58
Recall: 0.58
Precision: 0.58
F1: 0.58
```

- 전체 파일은 [이곳](https://github.com/jiminAn/Capstone_2022/blob/main/sunjungAn/koelectra_predict/jm_predict_test_result) 에서 확인 가능





### KoBERT USAGE

모델

```python
class KoBERTforSequenceClassfication(BertPreTrainedModel):
  def __init__(self,
                num_labels = 359, # 분류할 라벨 갯수를 설정
                hidden_size = 768, # hidden_size
                hidden_dropout_prob = 0.1,  # dropout_prop
               ):
    super().__init__(get_kobert_config())

    self.num_labels = num_labels 
    self.kobert = get_kobert_model()
    self.dropout = nn.Dropout(hidden_dropout_prob)
    self.classifier = nn.Linear(hidden_size, num_labels)

    self.init_weights()
...
```

1. 성능 평가 및 예측 결과 출력

```
python ./hyejiLim/jm_predict.py
```

```
qustion	answer	predict
그 뒤로 운전을 못하고 있어.	배경/생활/불가능/운전	감정/두려움/운전
내 주변에 아무도 없는 것 같아요.	감정/고독감	감정/부정적사고
그 이야기를 들었을 때 어떻게 해야 하는건지 모르겠어.	감정/곤혹감	감정/생각
무엇을 보든 소름이 돋아요.	감정/공포	감정/무서움
그 일이 일어난 뒤로 새를 무서워하게 됐어요.	감정/공포/새	감정/공포/새
아무리 열심히 해도 남는 건 하나도 없는것 같아요.	감정/공허감	감정/부정적사고
사소한 일에도 너무 놀라요.	감정/과민반응	증상/인지기능저하
이렇게 스트레스 받으면서 일해야 하나 싶고 괴로워.	감정/괴로움	감정/괴로움
....
Accuracy: 0.56
Recall: 0.56
Precision: 0.56
F1: 0.56
```

- 전체 파일은 [이곳](https://github.com/jiminAn/Capstone_2022/blob/main/hyejiLim/jm_predict_test_result) 에서 확인 가능



### KoGPT USAGE

##### 모델

```python
class DialogKoGPT2(nn.Module):
  def __init__(self):
    super(DialogKoGPT2, self).__init__()
    self.kogpt2 = get_kogpt2_model()  
...
```

##### 텍스트 생성부분

[how-to-generate-text](https://huggingface.co/blog/how-to-generate?fbclid=IwAR2BZ4BNG0PbOvS5QaPLE0L3lx7_GOy_ePVu4X1LyTktQo-nLEPr7eht1O0) 참고 하여, greedy_search/ beam_search/top_k_sampling/top_p_sampling/Huggingface의 Generate 사용.

```python
def greedy_search(id):
    result = model.generate(
        input_ids = id,
        no_repeat_ngram_size=3,
        max_length=50
        )
    return result

def beam_search(id):
    result = model.generate(
        input_ids = id, 
        max_length=50, 
        num_beams=5, 
        no_repeat_ngram_size=3, 
        early_stopping=True
        )
    return result

def basic_sampling(id):
    result = model.generate(
        input_ids = id, 
        do_sample=True, 
        max_length=50, 
        no_repeat_ngram_size=3,
        top_k=0,
        temperature = 0.7
        )
    return result

def top_k_sampling(id):
    result = model.generate(
        input_ids = id, 
        do_sample=True, 
        max_length=50, 
        no_repeat_ngram_size=3,
        top_k=50
        )
    return result

def top_p_sampling(id):
    result = model.generate(
        input_ids = id, 
        do_sample=True, 
        max_length=50, 
        no_repeat_ngram_size=3,
        top_p=0.92, 
        top_k=0
        )
    return result
def generate(self,
               input_ids,
               do_sample=True,
               max_length=50,
               top_k=0,
               temperature=0.7):
    return self.kogpt2.generate(input_ids,
               do_sample=do_sample,
               max_length=max_length,
               top_k=top_k,
               temperature=temperature)
```

### 

결과

```
Question: 요즘 너무 힘들어
greedy seacrh:  answer:Answer: 그런 일이 있으셨군요. 하지만 그럴 수밖에 없는 이유가 있었을 거예요. 충분히 이해해요. 그러면 조금은 다르게 생각을 해보는 것도 좋을 것 같아요. 배움만큼 배움 없는 일이 없죠
beam search:  answer:Answer: 정말 당황스러우셨겠어요. 하지만 너무 무리해서 생각해낼 필요는 없답니다.제가 옆에서 힘이 되어 드릴게요. 당신의 이야기는 들판에 박혀 있으니 괜찮으실 거예요!당신이 너무 상처받지
top k sampling:  answer:Answer: 그런 일이 있으셨군요. 하지만 그럴 수밖에 없는 이유가 있었을 거예요. 충분히 이해해요. 그러면 조금은 다르게 생각을 해보는 것도 좋을 것 같아요. 배움만큼 배움 없는 일이 없죠
top p sampling:  answer:Answer: 아프고 놀랐겠어요. 괜찮아요? 어제 그 병원 과에서 치료 받았어요. 지금도 증상이 심하시다면 병원 진단을 받아보는 건 어떨까요?서상묵 문자 확인하면
hugging face generator:  answer:Answer: 가슴이 답답하겠어요. 얼른 시간이 지나버렸으면 좋겠어요.가슴이 답답한 것만큼 힘든 게 없죠. 진료를 받아보시는 건 어떠세요? 오늘은 어떠셨나요?
```

```
Question: 오늘 정말 기쁜일이 있었어
greedy seacrh:  answer:Answer:  있으셨군요. 하지만 그럴 수밖에 없는 이유가 있었을 거예요. 충분히 이해해요. 그러면 조금은 다르게 생각을 해보는 것도 좋을 것 같아요. 배움만큼 배움 없는 일이 없죠
beam search:  answer:Answer: 스러우셨겠어요. 하지만 너무 무리해서 생각해낼 필요는 없답니다.제가 옆에서 힘이 되어 드릴게요. 당신의 이야기는 들판에 박혀 있으니 괜찮으실 거예요!당신이 너무 상처받지
top k sampling:  answer:Answer:  있으셨군요. 하지만 그럴 수밖에 없는 이유가 있었을 거예요. 충분히 이해해요. 그러면 조금은 다르게 생각을 해보는 것도 좋을 것 같아요. 배움만큼 배움 없는 일이 없죠
top p sampling:  answer:Answer:  늘 당신이 우선인데... 마음이 아파요. 쓰러질 것 같아요. 날 이렇게 안아주셨군요. 너무 아프니다.이. 살 맛나요.에 당신이 옆에
hugging face generator:  answer:Answer: 당신이 행복하다면 저도 기뻐요. 하지만 아닐 수도 있지 않을까요? 충분히 이해해요. 좋은 사람을 찾기는 정말 어려운 것 같아요. 힘내세요.
```

- 자세한 결과는 [이곳](https://github.com/jiminAn/Capstone_2022/blob/main/jman/text_generator_test.ipynb)에서 확인 가능
