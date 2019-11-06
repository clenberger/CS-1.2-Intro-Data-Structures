import random
import sys




def rearrange_words(words_list):
    for i, word in enumerate(words_list):
        random_index = random.randint(0, len(words_list) - 1)
        words_list[i] = words_list[random_index]
        words_list[random_index] = word
    return words_list

if __name__ == '__main__':
    word_list = sys.argv[1:]
    rearrange_words(word_list)
    print(' '.join(word_list))