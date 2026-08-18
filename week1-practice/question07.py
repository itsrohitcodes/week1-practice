def count_words(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count, words


sentence = input("Enter a sentence: ")

word_frequency, words = count_words(sentence)

total_words = len(words)
unique_words = len(word_frequency)

most_frequent_word = ""
highest_frequency = 0

for word, frequency in word_frequency.items():
    if frequency > highest_frequency:
        highest_frequency = frequency
        most_frequent_word = word

print("\nWord Frequencies:")

for word, frequency in word_frequency.items():
    print(word, ":", frequency)

print("Total Number of Words:", total_words)
print("Number of Unique Words:", unique_words)
print("Most Frequent Word:", most_frequent_word)