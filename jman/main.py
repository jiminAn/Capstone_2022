from model.kogpt2 import DialogKoGPT2
from kogpt2_transformers import get_kogpt2_tokenizer
import sys

max_length = 30
keyword = '혜지는'

def greedy_search(id):
    result = model.generate(
        input_ids = id,
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
        top_k=0,
        temperature = 0.7,
        no_repeat_ngram_size=3
        )
    return result

def top_k_sampling(id):
    result = model.generate(
        input_ids = id, 
        do_sample=True, 
        max_length=50, 
        top_k=50,
        no_repeat_ngram_size=3
        )
    return result

def top_p_sampling(id):
    result = model.generate(
        input_ids = id, 
        do_sample=True, 
        max_length=50, 
        top_p=0.92, 
        top_k=0,
        no_repeat_ngram_size=3
        )
    return result
    

if __name__ == '__main__':
    tokenizer = get_kogpt2_tokenizer()
    id = tokenizer.encode(keyword, add_special_tokens=False, return_tensors="pt")
    model = DialogKoGPT2()
    #result = greedy_search(id)
    #result = beam_search(id)
    #result = basic_sampling(id)
    #result = top_k_sampling(id)
    result = top_p_sampling(id)
    for generated_sequence in result:
        generated_sequence = generated_sequence.tolist()
    print("GENERATED SEQUENCE : {0}".format(tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)))