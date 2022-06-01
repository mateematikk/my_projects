from itertools import compress


def process_word(word):
    symbol_mask = [l.isalpha() for l in word]
    letters_rev = list(compress(word, symbol_mask))
    symbols = list(compress(word, [not e for e in symbol_mask]))
    word = ''.join(symbols.pop(0) if not e else letters_rev.pop() for e in symbol_mask)
    return word


def my_function(Sentence):
    reverseSentence = ' '.join(map(process_word, Sentence.split(' ')))
    return reverseSentence



