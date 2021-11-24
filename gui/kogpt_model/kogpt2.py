import torch.nn as nn

from jman.kogpt2_transformers import get_kogpt2_model


class DialogKoGPT2(nn.Module):
  def __init__(self):
    super(DialogKoGPT2, self).__init__()
    self.kogpt2 = get_kogpt2_model()

  def greedy_search(self,id):
      result = self.kogpt2.generate(
          input_ids=id,
          no_repeat_ngram_size=4,
          max_length=100
      )
      return result

  def basic_sampling(self,id):
      result = self.kogpt2.generate(
          input_ids=id,
          do_sample=True,
          max_length=100,
          no_repeat_ngram_size=4,
          top_k=0,
          temperature=0.7
      )
      return result

  def top_k_sampling(self,id):
      result = self.kogpt2.generate(
          input_ids=id,
          do_sample=True,
          max_length=100,
          no_repeat_ngram_size=4,
          top_k=50
      )
      return result

  def top_p_sampling(self,id):
      result = self.kogpt2.generate(
          input_ids=id,
          do_sample=True,
          max_length=100,
          no_repeat_ngram_size=4,
          top_p=0.92,
          top_k=0
      )
      return result

  # huggingface generator
  def generate(self,
               input_ids,
               do_sample=False,
               max_length=100,
               top_p=0,
               top_k=0,
               temperature= 1,
               no_repeat_ngram_size=4,
               num_return_sequences=1,
               num_beams = 1,
               early_stopping=False,
               ):
    return self.kogpt2.generate(input_ids,
               num_beams = num_beams,
               do_sample=do_sample,
               max_length=max_length,
               top_p = top_p,
               top_k=top_k,
               temperature=temperature,
               no_repeat_ngram_size= no_repeat_ngram_size,
               num_return_sequences=num_return_sequences,
               early_stopping = early_stopping,
              )

  def forward(self, input, labels = None):
    if labels is not None:
      outputs = self.kogpt2(input, labels=labels)
    else:
      outputs = self.kogpt2(input)

    return outputs

