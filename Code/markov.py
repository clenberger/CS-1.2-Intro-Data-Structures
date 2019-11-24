from histograms import histogram, book
from sample import sample_dict
from random import choice  




def build_markov(words_list):
    markov = {}
    for index, word in enumerate(words_list):
        if word not in markov:
            if index < len(words_list) - 1:
                markov[word] = [words_list[index + 1]]
        elif word in markov:
            if index < len(words_list) - 1:
                markov[word].append(words_list[index + 1])
                
    for key in markov:
        markov[key] = histogram(markov[key])
    return markov
        
        
def build_markov_sentence(markov, length):
    sentence = []
    sentence.append(choice(list(markov.keys())))
    for i in range(0, length - 1):
        sentence.append(sample_dict(markov[sentence[i]]))
    return ' '.join(sentence)





if __name__ == "__main__":
	import sys
	arguments = sys.argv[1:]
	words_list = book(arguments[0])
	markov = build_markov(words_list)
	print(build_markov_sentence(markov, 10))
