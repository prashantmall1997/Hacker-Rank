# https://www.hackerrank.com/challenges/repeated-string/problem

from math import ceil


def repeatedString(string, upto):
    count = 0
    extra = upto - upto//len(string)*len(string)
    whole = upto//len(string)
    for letter in range(0, len(string)):
        if string[letter] == "a":
            count = count + whole
            if letter+1 <= extra:
                count += 1

    return count


string = input()
upto = int(input())

result = repeatedString(string, upto)
print(result)
