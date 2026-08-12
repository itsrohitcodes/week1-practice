# Function-Based Word Frequency Analyzer

def count_words(sentence):
    sentence = sentence.lower()
    words = sentence.split()

    word_count = {}

    for i in words:
        if i in word_count:
            word_count[i] = word_count[i] + 1
        else:
            word_count[i] = 1

    return word_count


sentence = input()

word_frequency = count_words(sentence)

total_words = len(sentence.split())

unique_words = len(word_frequency)

most_frequent_word = ""
highest_frequency = 0

for i in word_frequency:
    if word_frequency[i] > highest_frequency:
        highest_frequency = word_frequency[i]
        most_frequent_word = i

print("Word Frequencies:")

for i in word_frequency:
    print(i, ":", word_frequency[i])

print("Total Number of Words:", total_words)
print("Number of Unique Words:", unique_words)
print("Most Frequent Word:", most_frequent_word)