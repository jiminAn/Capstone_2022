## category_slicing

### Object


감정/걱정/건강염려 | 수술도 잘 됐고, 의사도 회복만 잘 하면 된다는데 자꾸   걱정이 돼요.
-- | --
감정/걱정/건강염려 | 원래 병에 잘 걸리지 않는 편이었는데, 한 번 심장이 이상하다고 느끼니까 건강 걱정이 늘었어요.
감정/걱정/건강염려 | 아, 내가 길 가다가 갑자기 확 쓰러지는 건 아닐까요?
감정/걱정/건강염려 | 병원에서 몸에 큰 이상이 있다고 하면 어떡하죠?
감정/걱정/건강염려 | 한번 그러고 나서는 건강 걱정이 많아졌어.
감정/걱정/건강염려 | 근데 너무 감정이입해서 봤는지, 나도 암에 걸리면 어떡하지라는 생각이 막 드는거에요.
감정/걱정/건강염려 | 큰 병이면 어떡하나 걱정 돼서 병원도 못 가겠어.
감정/걱정/건강염려 | 계속 병원에만 있다 보니까 진짜 문제 있을까봐 걱정이야.
감정/걱정/건강염려 | 몸에 무슨 문제 있는 건가 걱정도 되고…
감정/걱정/건강염려 | 어딘가 잘못됐을까요?
감정/걱정/건강염려 | 다른 병원에 가서 진찰을 좀 더 받아보는 게 맞을까?
감정/걱정/경제적문제 | 학자금은 언제 다 갚나… 아직도 몇 년은 더 남았는데…
감정/걱정/경제적문제 | 경제적인 문제만 좀 풀려주면 좋겠는데… 쉽지가 않네요.
감정/걱정/경제적문제 | 언제쯤 저는 돈 걱정 없이 살 수 있을까요?
감정/걱정/경제적문제 | 내가 나중에 이걸 관두면 나는 그럼 어떡하지? 뭘 해 먹고 살지? 돈은?
감정/걱정/경제적문제 | 당장 해결해야 하는 치료비 때문에 걱정이 많았어.
감정/걱정/경제적문제 | 걱정이 되게 많았거든요. 등록금도 그렇고 생활비도 그렇고… 다 돈 문제…
감정/걱정/경제적문제 | 당장 다음 달 월세도 내야 하고 그런데… 아무래도 돈 걱정이 제일 커.
감정/걱정/경제적문제 | 근데 그것도 잠시였고 한 달만 지나니까 막 돈 걱정이 되는 거예요.



위의 표의 카테고리들을 최대 대분류/중분류 까지만 잘라 따로 저장하는 코드

결과물로는 아래 2개의 파일이 생성된다. 

### category_index.csv


0 | 감정/감정조절이상
-- | --
1 | 감정/걱정
2 | 감정/고독감
3 | 감정/곤혹감
4 | 감정/공포
5 | 감정/공허감
6 | 감정/과민반응
7 | 감정/괴로움
8 | 감정/기분저하
9 | 감정/기시감
10 | 감정/긴장
11 | 감정/눈물
12 | 감정/답답
13 | 감정/당황
14 | 감정/두려움
15 | 감정/멍함
16 | 감정/모호함
17 | 감정/무력감
### category_question.csv
감정/걱정 | 또 실수하지는 않았을까, 걱정이 들어요.
-- | --
감정/걱정 | 아침에 눈뜨면 오늘은 뭘 해야 할지 걱정부터 들어요.
감정/걱정 | 성격이 불같아서 걱정이에요.
감정/걱정 | 다른 때는 그래도 괜찮은데 수업할 때도 이럴까봐 너무 걱정이야.
감정/걱정 | 요즘 들어 내가 그런 거 아닌 건가 싶어서 걱정 된다니까.
감정/걱정 | 그래서 더 걱정되는 것 같기도 해요.
감정/걱정 | 진짜 걱정이 이만저만이 아니다…
감정/걱정 | 안 해도 되는 걱정을 굳이 사서 하는 편이라 더 그랬어요.
감정/걱정 | 근데 이거 때문에 좀 걱정이 많아요.
감정/걱정 | 딱히 스트레스 받는 건 없었는데 진짜 그런 문제였던 건가 싶어서 걱정돼.
감정/걱정 | 앞으로 나는 뭘 해 먹고 사나 같은 이런저런 걱정이 들고…
감정/걱정 | 앞으로 난 뭘 해야 할까, 내가 뭘 잘 하긴 하는 걸까 걱정이 많았거든요.
감정/걱정 | 무슨 문제가 있는 건 아닐까 싶어서 걱정이 돼요.



## 실행 순서
1. file_download.py
> google drive에 있는 wellness 데이터셋을 다운받는다.
2. xlsx_to_csv.py
> 다운 받는 wellness 데이터셋을 csv파일 형태로 변환해준다.
3. category_question.py
> 변환한 csv파일을 가지고, category_index.csv, category_question.csv파일을 만들어 저장한다. 