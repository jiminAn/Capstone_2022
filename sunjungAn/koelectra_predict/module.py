import torch
import torch.nn as nn
import random
from transformers import (
  ElectraConfig,
  ElectraTokenizer,
  
)
from transformers.models.electra import tokenization_electra
from koelectra import koElectraForSequenceClassification,koelectra_input
#from model.kobert import KoBERTforSequenceClassfication, kobert_input
from kobert_transformers import get_tokenizer


class DialogElectra:
    def __init__(self):
        self.checkpoint_path ="./checkpoint"
        self.save_ckpt_path = "koelectra-wellnesee-text-classification.pth"
        model_name_or_path = "monologg/koelectra-base-discriminator"

        # 답변과 카테고리 불러오기
        self.category, self.answer = load_wellness_answer()

        ctx = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(ctx)

        # 저장한 Checkpoint 불러오기
        checkpoint = torch.load(self.save_ckpt_path, map_location=self.device)

        # Electra Tokenizer
        self.tokenizer = ElectraTokenizer.from_pretrained(model_name_or_path)

        electra_config = ElectraConfig.from_pretrained(model_name_or_path)
        self.model = koElectraForSequenceClassification.from_pretrained(pretrained_model_name_or_path=model_name_or_path,
                                                                   config=electra_config,
                                                                   num_labels=359)
        self.model.load_state_dict(checkpoint['model_state_dict'],strict=False)
        self.model.to(self.device)
        self.model.eval()

    def predict(self, sentence):

        data = koelectra_input(self.tokenizer, sentence, self.device, 512)
        # print(data)

        output = self.model(**data)

        logit = output
        softmax_logit = nn.Softmax(logit).dim
        softmax_logit = softmax_logit[0].squeeze()

        max_index = torch.argmax(softmax_logit).item()
        max_index_value = softmax_logit[torch.argmax(softmax_logit)].item()

        answer_list = self.answer[self.category[str(max_index)]]
        answer_len = len(answer_list) - 1
        answer_index = random.randint(0, answer_len)

        #return answer_list
        #return self.category[str(max_index)]
        return max_index




def load_wellness_answer():
  root_path = '..'
  category_path = "./data/wellness_dialog_category.txt"
  answer_path = "./data/wellness_dialog_answer.txt"

  c_f = open(category_path,'r', encoding="utf-8" )
  a_f = open(answer_path,'r', encoding="utf-8" )

  category_lines = c_f.readlines()
  answer_lines = a_f.readlines()

  category = {}
  answer = {}
  for line_num, line_data in enumerate(category_lines):
    data = line_data.split("\t")
    category[data[1][:-1]]=data[0]

  for line_num, line_data in enumerate(answer_lines):
    data = line_data.split("\t")
    keys = answer.keys()
    if(data[0] in keys):
      answer[data[0]] += [data[1][:-1]]
    else:
      answer[data[0]] =[data[1][:-1]]

  return category, answer

