# -*- coding: utf-8 -*-
"""assignment_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/122LsqoJXjjDt8nA_3WaaLozRLnXoSrqj
"""

import random
from collections import defaultdict

def build_markov_chain(text):
    words = text.split()
    chain = defaultdict(list)

    for current_word, next_word in zip(words, words[1:]):
        chain[current_word].append(next_word)

    return chain

def generate_text(markov_chain, length=50, seed=None):
    if seed is not None:
        random.seed(seed)

    current_word = random.choice(list(markov_chain.keys()))
    generated_text = [current_word]

    for _ in range(length - 1):
        next_word = random.choice(markov_chain[current_word])
        generated_text.append(next_word)
        current_word = next_word

    return ' '.join(generated_text)

# Example usage
text_data = "Your input text data here..."
markov_chain = build_markov_chain(text_data)

generated_text = generate_text(markov_chain, length=50, seed=42)
print(generated_text)