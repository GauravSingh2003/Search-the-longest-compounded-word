import time

# Step 1: Read the input file and store the words
def read_words_from_file(file_name):
    with open(file_name, 'r') as file:
        words = [line.strip() for line in file]

    return

input_file = 'Input.txt'
words = read_words_from_file(input_file)

# Step 2: Sort the words in descending order of length
words.sort(key=len, reverse=True)

import time

# Step 1: Read the input file and store the words
def read_words_from_file(file_name):
    with open(file_name, 'r') as file:
        words = [line.strip() for line in file]

    return

input_file = 'Input_01.txt'
words = read_words_from_file(input_file)

# Step 2: Sort the words in descending order of length
words.sort(key=len, reverse=True)

# Step 3, 4: Identify the longest compounded words
def is_compounded(word, word_set):
    if word in word_set:
        return True

    for i in range(1, len(word)):
        prefix, suffix = word[:i], word[i:]
        if prefix in word_set and is_compounded(suffix, word_set):
            return True

    return False

def get_longest_compounded_words(words):
    longest_word = ""
    second_longest_word = ""
    word_set = set(words)

    for word in words:
        if is_compounded(word, word_set):
            if len(word) > len(longest_word):
                second_longest_word = longest_word
                longest_word = word
            elif len(word) > len(second_longest_word):
                second_longest_word = word
        return longest_word, second_longest_word

import time

# Step 1: Read the input file and store the words
def read_words_from_file(file_name):
    with open(file_name, 'r') as file:
        words = [line.strip() for line in file]

    return

input_file = 'Input_01.txt'
words = read_words_from_file(input_file)

# Step 2: Sort the words in descending order of length
words.sort(key=len, reverse=True)

# Step 3, 4: Identify the longest compounded words
def is_compounded(word, word_set):
    if word in word_set:
        return True

    for i in range(1, len(word)):
        prefix, suffix = word[:i], word[i:]
        if prefix in word_set and is_compounded(suffix, word_set):
            return True

    return False

def get_longest_compounded_words(words):
    longest_word = ""
    second_longest_word = ""
    word_set = set(words)

    for word in words:
        if is_compounded(word, word_set):
            if len(word) > len(longest_word):
                second_longest_word = longest_word
                longest_word = word
            elif len(word) > len(second_longest_word):
                second_longest_word = word

    return longest_word, second_longest_word

longest_compounded_word, second_longest_compounded_word = get_longest_compounded_words(words)

# Step 5: Measure the time taken to process the input file
start_time = time.time()

# Your code to process the input file

end_time = time.time()
time_taken = end_time - start_time

# Display the results
print("Longest compounded word: ", longest_compounded_word)
print("Second longest compounded word: ", second_longest_compounded_word)
print("Time taken: ", time_taken, " seconds")
