# question 07

# Function to count words
def count_words(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count, words

# Input the sentence
sentence = input()

# Function call
word_frequency, words = count_words(sentence)

total_words = len(words)
unique_words = len(word_frequency)

most_frequent_word = ""
highest_frequency = 0

# Find the most frequent word
for word, frequency in word_frequency.items():
    if frequency > highest_frequency:
        highest_frequency = frequency
        most_frequent_word = word

# Print the results
print("Word Frequencies:")

for word, frequency in word_frequency.items():
    print(word, ":", frequency)

print(f"Total Number of Words: {total_words}")
print(f"Number of Unique Words: {unique_words}")
print(f"Most Frequent Word: {most_frequent_word}")