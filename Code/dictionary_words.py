#Thanks to Mark Kim for helping me build this out
import sys
from random import choice


def random_dictionary_words(amount):
    with open('/usr/share/dict/words') as file:
        word_list = file.readlines()
        count = 0 
        random = []
        while count < int(amount):
            random.append(choice(word_list).strip())
            count += 1
        
    return ' '.join(random)
    
    
    
    
if __name__ == '__main__':
    amount = sys.argv[1]
    output = random_dictionary_words(amount)
    print(output + ".")
