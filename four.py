from typing import List, Callable


def alphabetize(word: str) -> str:
    return ''.join(sorted(word))


def contains_no_duplicate_words(passphrase: str) -> bool:
    words = passphrase.split()
    return len(set(words)) == len(words)


def contains_no_anagram_words(passphrase: str) -> bool:
    words = [alphabetize(word) for word in passphrase.split()]
    return len(set(words)) == len(words)


def valid_passphrases(file_input: str, validator: Callable[[str], bool]) -> List[bool]:
    passphrases = file_input.split('\n')
    return [validator(passphrase) for passphrase in passphrases]


# Part 1
tests = '''aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa'''
print(valid_passphrases(tests, contains_no_duplicate_words))     # [True, False, True]


puzzle_input = open('four-input.txt', 'r').read()
valid = valid_passphrases(puzzle_input, contains_no_duplicate_words)
print(len([p for p in valid if p]))     # number of valid passwords


# Part 2
tests = '''abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio'''
print(valid_passphrases(tests, contains_no_anagram_words))     # [True, False, True, True, False]


valid = valid_passphrases(puzzle_input, contains_no_anagram_words)
print(len([p for p in valid if p]))     # number of valid passwords
