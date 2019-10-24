import random
import sys


words = []

def rearrange_words(words):
    rearranged_words = list()
    while not len(rearranged_words) == len(words):
        rand_index = random.randint(0, len(words) - 1)
        random_word = words[rand_index]
        if random_word not in rearranged_words:
            rearranged_words.append(random_word)
    for word in rearranged_words:
        print(word, end=" ")



if __name__ == '__main__':
    words = sys.argv[1:]
    rearrange_words(words)