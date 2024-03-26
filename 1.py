def read_file_with_limit():
    with open('C:\\Users\\User\\Desktop\\text.txt', 'r') as file:
        for line in file:
            if len(line) > 20:
                yield line[:20]
            else:
                yield line

def reverse_words(line):
    words = line.split()
    reversed_words = []
    for word in reversed(words):
        reversed_words.append(word)
    return ' '.join(reversed_words)

lines_with_limit = read_file_with_limit()

reversed_lines = map(reverse_words, lines_with_limit)

for line in reversed_lines:
    print(line)
