# Question 42 - Sentiment analysis for app reviews

# You are given an array containing reviews for a popular iOS app below:

# reviews = [‘app is good, but forced updates are too frequent‘, ‘love this app, use it daily to log calories', 'free version of this app has way too many ads’, ‘app doesn't load, 0/10’]

# Your task is to determine sentiment from the review above. To do this you first decide to write code to find the count of individual words across all the reviews -- write this code using Python.

# Upgrade to premium to receive in-depth solutions to each problem.


def count_words_in_strings(strings):
    words = set()
    for item in strings:
        for word in item.split(" "):
            words.add(word)
    return len(words)

# i like this problem, it requires data structure knowledge to get teh right
# solution but is easy to code up if you're knowledgeable


# i think i should understand the problem as wanting the count of each word
def count_each_word(strings):
    word_count = {}
    for item in strings:
        for word in item.split(" "):
            word_count[word] = word_count.get(word, 0) + 1
    return word_count
