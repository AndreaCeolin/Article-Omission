from collections import Counter
import sys


def main(input_file, n):
    count_dict = Counter()
    with open(input_file, 'r', encoding="utf8") as f:
        text = f.read().splitlines()
        for line in text:
            new_line = line.split()
            if new_line[1] == 'NN':
                count_dict[new_line[0]] += 1
    for word, count in count_dict.most_common(int(n)):
        print(word, count)

if __name__ == "__main__":
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print('Syntax: input_file n')