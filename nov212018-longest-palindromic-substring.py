# Question 58 - Longest palindrome substring

# A palindrome is "a word, phrase, or sequence that reads the same backward as forward." Below are some example palindromes:

#     madam
#     racecar
#     tat

# Can you write a python function that takes in a string and outputs the longest palindrome? If the string itself is a palindrome, the function would output the original string.

# Upgrade to premium to receive in-depth solutions to each problem.


def is_palindrome(word):
    if word != '':
        return all(a == b for a, b in zip(word[:int(len(word)/2)],
                                          word[-int(len(word)/2):][::-1]))
    return False


def get_longest_palindromic_substring(word):
    longest_palindrome = ''
    for i in range(int(len(word))):
        for j in range(i, int(len(word))+1):
            if is_palindrome(word[i:j]) and j - i > len(longest_palindrome):
                longest_palindrome = word[i:j]
    return longest_palindrome


if __name__ == "__main__":
    glps = get_longest_palindromic_substring
    print(glps('racecar'))
    print(glps('truther'))
    print(glps("ayy lmao"))
    print(glps('tatoo'))
    print(glps('madamoiselle'))
