#! /bin/env python3

f = open('day5_data.txt', mode='r')

nice_words_old = 0
nice_words_new = 0
word = f.readline()[:-1]


# This function verifies 3 unique vowels, we need 3 total vowels
#def three_vowels(test_word):
#    vowels = 0
#    if 'a' in test_word:
#        vowels += 1
#    if 'e' in test_word:
#        vowels += 1
#    if 'i' in test_word:
#        vowels += 1
#    if 'o' in test_word:
#        vowels += 1
#    if 'u' in test_word:
#        vowels += 1
#
#    if vowels >= 3:
#        return True
#    else:
#        return False

#############
# Old Rules #
#############

def three_vowels(test_word):
    vowels = 0
    vowels += test_word.count('a')
    vowels += test_word.count('e')
    vowels += test_word.count('i')
    vowels += test_word.count('o')
    vowels += test_word.count('u')

    if vowels >= 3:
        return True
    else:
        return False

def appears_twice(test_word):
    result = False
    #Set last letter to the first letter of the string
    last_letter = test_word[:1]
    # Loop over every letter except the first
    for this_letter in test_word[1:]:
        if last_letter == this_letter:
            result = True
            break
        else:
            last_letter = this_letter
    return result

def restricted_strings(test_word):
    result = False
    restricted_list = ['ab','cd','pq','xy']

    for restricted in restricted_list:
        if restricted in test_word:
            result = True
            break
    return result

def is_nice_old(test_word):
    return three_vowels(test_word) and appears_twice(test_word) and not restricted_strings(test_word) 

#############
# New rules #
#############

def two_letters_twice(test_word):
    result = False
    for index in range(len(test_word) - 1):
        test_letters = test_word[index:index + 2]
        #I thought I would need to add a case to invalidate 'aaa' but python returns 'aaa'.count('aa') as 1
        if test_word.count(test_letters) >= 2:
            result = True
            break
    return result

def one_letter_repeat(test_word):
    result = False
    for index in range(len(test_word) - 2):
        test_letter = test_word[index]
        if test_letter == test_word[index + 2]:
            result = True
            break
    return result

def is_nice_new(test_word):
    return two_letters_twice(test_word) and one_letter_repeat(test_word)

while word != '':
    if is_nice_old(word):
        nice_words_old += 1
    if is_nice_new(word):
        nice_words_new += 1
    #print(word + ' Is nice: ' + str(is_nice(word)))
    #print('Three vowels: ' + str(three_vowels(word)))
    #print('Consecutive letters: ' + str(appears_twice(word)))
    #print('Contains ab, cd, pq, xy: ' + str(restricted_strings(word)))
    word = f.readline()[:-1]

print('Nice words - old rules: ' + str(nice_words_old))
print('Nice words - new rules: ' + str(nice_words_new))
