# Given two words of equal length that are in a dictionary, write a method to transform one word into another word by changing only
# one letter at a time.  The new word you get in each step must be in the
# dictionary.

# def transform(english_words, start, end):

# transform(english_words, 'damp', 'like')
# ['damp', 'lamp', 'limp', 'lime', 'like']
# ['damp', 'camp', 'came', 'lame', 'lime', 'like']


def is_diff_one(str1, str2):
    if len(str1) != len(str2):
        return False

    count = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count = count + 1

    if count == 1:
        return True

    return False


potential_ans = []


def transform(english_words, start, end, count):
    global potential_ans
    if count == 0:
        count = count + 1
        potential_ans = [start]

    if start == end:
        print (potential_ans)
        return potential_ans

    for w in english_words:
        if is_diff_one(w, start) and w not in potential_ans:
            potential_ans.append(w)
            transform(english_words, w, end, count)
            potential_ans[:-1]

    return None


english_words = set(['damp', 'camp', 'came', 'lame', 'lime', 'like'])
transform(english_words, 'damp', 'lame', 0)
