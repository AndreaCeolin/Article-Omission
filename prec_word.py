import sys
from collections import Counter

#Find elements pre- post- word, return elements ordered by frequency
def context(input_file, element):
    #Collect pre- and post-element in a dictionary with frequencies
    word_dict = Counter()
    tokenized_words = [line.split() for line in open(input_file, 'r', encoding="utf8")]
    for index, line in enumerate(tokenized_words):
        if line[0] == element and (line[1] == 'NC' or line[1] == 'NN' or line[1] == 'NOM'):
            if tokenized_words[index-1][0] == '%' or tokenized_words[index-1][0] == '[' or tokenized_words[index-1][0] == ']' or tokenized_words[index-1][0] == '(':
                continue
            elif tokenized_words[index-1][1] != 'ADJ' and tokenized_words[index-1][1] != 'JJ' and tokenized_words[index-1][1] != 'ADJA' and tokenized_words[index-1][1] != 'ADJD':
                word_dict[tokenized_words[index-1][0]] += 1
            else:
                word_dict[tokenized_words[index-2][0]] += 1
    print(sum(word_dict.values()))
    for number, word in word_dict.most_common():
        print(number,word)


if __name__ == "__main__":
    try:
        context(sys.argv[1], sys.argv[2])
    except IndexError:
        print('ERROR: prec_word.py file word')


