import torch
from model.kogpt2 import DialogKoGPT2
from model.kogpt2_transformers import get_kogpt2_tokenizer

class answer_generator:
  def __init__(self):
    self.save_ckpt_path = f"./model/checkpoint/kogpt2-data2_3_ep10.pth"
    self.ctx = "cuda" if torch.cuda.is_available() else "cpu"
    self.device = torch.device(self.ctx)
    # 저장한 Checkpoint 불러오기
    self.checkpoint = torch.load(self.save_ckpt_path, map_location=self.device)

    self.model = DialogKoGPT2()
    self.model.load_state_dict(self.checkpoint['model_state_dict'])

    self.model.eval()
    self.tokenizer = get_kogpt2_tokenizer()
    self.output_size = 200 # 출력하고자 하는 토큰 갯수

  def get_answer(self, question):
    tokenized_indexs = self.tokenizer.encode(question)

    input_ids = torch.tensor([self.tokenizer.bos_token_id,]  + tokenized_indexs +[self.tokenizer.eos_token_id]).unsqueeze(0)
    result = self.model.generate(input_ids=input_ids)
    return self.tokenizer.decode(result[0].tolist()[len(tokenized_indexs)+1:],skip_special_tokens=True)
