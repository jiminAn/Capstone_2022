import torch

from gui.kobert_model.load_kobert import DialogKoBERT



class question_classificator:
  def __init__(self):
    self.kobert = DialogKoBERT()
    self.q_category = ""

  def get_question_category(self, question):
    self.q_category = self.kobert.predict(question)
    return self.q_category