from model.load_kobert import DialogKoBERT
from model.load_kogpt2 import answer_generator
import string
import time

kobert = None
kogpt2 = None

def setup():
    global kobert, kogpt2
    kobert = DialogKoBERT()
    kogpt2 = answer_generator()

def get_question():
    # check sqs
    question = 'This is Question'
    return question

def set_answer(dialog_answer, category_answer):
    # send to sqs
    pass

def trim_text(text):
    sentence_count = 0
    last = -1
    for idx, char in enumerate(text):
        if char in string.punctuation:
            if char == ',':
                continue
            last = idx
            sentence_count += 1
            if sentence_count == 1:
                break
    return text[:last + 1]


if __name__=='__main__':
    # 시작
    setup()
    while True:
        try:
            q = get_question()
            a_dialog = kogpt2.get_answer(trim_text(q))
            a_category = kobert.predict(q)     
            set_answer(a_dialog, a_category)
        except:
            set_answer('Error', 'Error')
            setup()
        time.sleep(0.25)