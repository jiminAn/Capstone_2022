import numpy as np
import gc
import torch
import torch.nn as nn
from torch.utils.data import Dataset
from kogpt2_transformers import get_kogpt2_tokenizer
from kobert_transformers import get_tokenizer
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
from tqdm import tqdm
import sys
#from tensorboardX import SummaryWriter
#summary = SummaryWriter()
#sys.path.append('drive/My Drive/Colab Notebooks/')
#sys.path.append('drive/My Drive/Colab Notebooks/dialogLM')

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
from tqdm import tqdm

import torch
from transformers import (
  AdamW,
  ElectraConfig,
  ElectraTokenizer
)
from torch.utils.data import dataloader
from model import koElectraForSequenceClassification
from dataloader import WellnessTextClassificationDataset
#from dialogLM.dataloader.wellness import WellnessTextClassificationDataset
#from dialogLM.model.koelectra import koElectraForSequenceClassification
from train import train
import tqdm
gc.collect()
torch.cuda.empty_cache()
data_path = "../data/wellness_chatbot_data (3).txt"
checkpoint_path =f"checkpoint"
save_ckpt_path = f"koelectra-wellnesee-text-classification10.pth"
model_name_or_path = "monologg/koelectra-base-discriminator"


n_epoch = 2         # Num of Epoch
batch_size = 32      # 배치 사이즈
ctx = "cpu"
device = torch.device(ctx)
save_step = 100 # 학습 저장 주기
learning_rate = 5e-6  # Learning Rate

# Electra Tokenizer
tokenizer = ElectraTokenizer.from_pretrained(model_name_or_path)

# WellnessTextClassificationDataset 데이터 로더
dataset = WellnessTextClassificationDataset(file_path=data_path, tokenizer=tokenizer, device=device)
train_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

electra_config = ElectraConfig.from_pretrained(model_name_or_path)
model = koElectraForSequenceClassification.from_pretrained(pretrained_model_name_or_path=model_name_or_path,
                                                            config=electra_config,
                                                            num_labels=359)
model.to(device)

# Prepare optimizer and schedule (linear warmup and decay)
no_decay = ['bias', 'LayerNorm.weight']
optimizer_grouped_parameters = [
    {'params': [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)],
      'weight_decay': 0.01},
    {'params': [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
]
optimizer = AdamW(optimizer_grouped_parameters, lr=learning_rate)

pre_epoch, pre_loss, train_step = 0, 0, 0
if os.path.isfile(save_ckpt_path):
    checkpoint = torch.load(save_ckpt_path, map_location=device)
    pre_epoch = checkpoint['epoch']
    pre_loss = checkpoint['loss']
    train_step =  checkpoint['train_step']
    total_train_step =  checkpoint['total_train_step']

    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

    print(f"load pretrain from: {save_ckpt_path}, epoch={pre_epoch}, loss={pre_loss}")
    # best_epoch += 1

losses = []
offset = pre_epoch
for step in range(n_epoch):
    epoch = step + offset
    loss = train( epoch, model, optimizer, train_loader, save_step, save_ckpt_path, train_step)
    #summary.add_scalar('loss', loss, step)
    losses.append(loss)

# data
data = {
    "loss": losses
}
df = pd.DataFrame(data)
display(df)

# graph
plt.figure(figsize=[12, 4])
plt.plot(losses, label="loss")
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()