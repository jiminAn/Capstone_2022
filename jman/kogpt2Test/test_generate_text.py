import torch
from dialogLM.Kogpt2 import DialogKoGPT2
from kogpt2_transformers import get_kogpt2_tokenizer
save_ckpt_path = './dialogLM/checkpoint/kogpt2-data2_1_ep5.pth'

assert torch.cuda.is_available()

ctx = "cuda" if torch.cuda.is_available() else "cpu"
device = torch.device(ctx)

model = DialogKoGPT2()
checkpoint = torch.load(save_ckpt_path, map_location=device)
model.load_state_dict(checkpoint['model_state_dict'])
model.eval()
tokenizer = get_kogpt2_tokenizer()
output_size = 200

questions = ["요즘 너무 힘들어", "계속 머리가 빠지는 것 같아", "죽고싶어", "오늘 정말 기쁜일이 있었어"]
t_idxs = [tokenizer.encode(q) for q in questions]
input_idxs = [torch.tensor([tokenizer.bos_token_id,]+t_idx+[tokenizer.eos_token_id]).unsqueeze(0) for t_idx in t_idxs]

for input_idx, t_idx in zip(input_idxs,t_idxs):
    result = model.generate(input_ids=input_idx)
    answer = tokenizer.decode(result[0].tolist()[len(t_idx)+1:],skip_special_tokens=True)
    print(answer)
