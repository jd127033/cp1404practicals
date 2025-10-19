"""
CP1404/CP5632 Practical
Word Occurrences using dictionaries
"""

# Create Dictionary
words_to_count = {}
sentence = "This is a example sentence with a repeated word in it"
terms = sentence.split()
# Iterate through terms to count the number of occurrences of each word in the sentence
# Better to ask for forgiveness than permission.
for word in terms:
    try:
        words_to_count[word] += 1
    except KeyError:
        words_to_count[word] = 1

#Check for the largest word in the sentence for formating
largest_length = max((len(word) for word in terms))

# Print the number of occurrences for each word
for word in sorted(words_to_count):
    print(f"{word:{largest_length}} : {words_to_count[word]}")


