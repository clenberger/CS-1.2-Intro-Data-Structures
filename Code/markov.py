from histograms import histogram, book
from sample import sample_dict
from random import choice  




def build_markov(words_list):
    markov = {}
    for index, word in enumerate(words_list):
        if word not in markov:
            if index < len(words_list) - 1:
                markov[word]