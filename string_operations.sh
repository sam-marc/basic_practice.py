#!/bin/bash

# Define the sentence
sentence="The quick brown fox jumps over the lazy dog"

# Convert the sentence to uppercase
uppercase_sentence=$(echo "$sentence" | tr '[:lower:]' '[:upper:]')

# Count the number of words in the sentence
word_count=$(echo "$sentence" | wc -w)

# Extract the first word from the sentence
first_word=$(echo "$sentence" | cut -d' ' -f1)

# Replace all occurrences of a specific word
modified_sentence=$(echo "$sentence" | sed 's/quick/lazy/g')

# Display the results
echo "Uppercase sentence: $uppercase_sentence"
echo "Number of words: $word_count"
echo "First word: $first_word"
echo "Modified sentence: $modified_sentence"
