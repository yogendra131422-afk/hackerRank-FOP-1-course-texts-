Strings programing questions and programing answers in python 



1 . Strings - Data Compression for Server Log Optimization
In a server system, large text-based log files are generated every second.
These logs often contain repetitive characters — for example, long sequences of the same event code or marker.

solution :
s = input()

# Compress by removing consecutive duplicates
compressed = ""
for i in range(len(s)):
    if i == 0 or s[i] != s[i-1]:
        compressed += s[i]

# Reverse the compressed string
result = compressed[::-1]
print(result)




2.Strings - Reversing Words for a Speech Teleprompter
A speech teleprompter displays the speaker’s script, but sometimes the text must be shown in reverse order of
words so that it can be read properly by the teleprompter’s mirror setup.
Your task is to write a Python program that reverses the order of words in a given sentence.
Each word in the sentence should remain unchanged, but their order should be reversed.

solution : 
s = input()

# Extract words without using split
words = []
current_word = ""
for char in s:
    if char == ' ':
        if current_word:
            words.append(current_word)
            current_word = ""
    else:
        current_word += char

# Don't forget the last word
if current_word:
    words.append(current_word)

# Reverse the words list
words.reverse()

# Build result with single spaces
result = ""
for i in range(len(words)):
    result += words[i]
    if i < len(words) - 1:
        result += " "

print(result)




3.Strings - Analyzing Sentence Complexity in Content Writing
Write a program to analyze a sentence and determine its complexity based on the number of words and sentence length.

solution :
s = input()

# Handle null/empty input
if not s or len(s.strip()) == 0:
    print(0)
else:
    vowels = set('aeiou')
    words = s.split()
    
    hard_count = 0
    easy_count = 0
    
    for word in words:
        # Count vowels and consonants
        vowel_count = 0
        consonant_count = 0
        
        for char in word:
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        
        # Check for 3+ consecutive consonants
        has_three_consecutive = False
        consecutive = 0
        for char in word:
            if char not in vowels:
                consecutive += 1
                if consecutive >= 3:
                    has_three_consecutive = True
                    break
            else:
                consecutive = 0
        
        # Determine if hard or easy
        if consonant_count > vowel_count or has_three_consecutive:
            hard_count += 1
        else:
            easy_count += 1
    
    # Calculate difficulty quotient
    difficulty = (5 * hard_count) - (2 * easy_count)
    print(difficulty)



4.Strings - Kindergarten Sentence Building
Write a program to rearrange a group of given words into a meaningful sentence, 
simulating how kindergarten children learn to form simple sentences.

solution :
sentence = input()
words = sentence.split()

max_length = 0
for word in words:
    alpha_count = sum(1 for char in word if char.isalpha())
    max_length = max(max_length, alpha_count)

print(max_length)




5.Strings - Analyzing Alphanumeric Characters in Official Documents
Write a program to analyze a given string and count how many letters,
digits, and special characters it contains in an official document.

solution : 
s = input()

# Handle empty input
if len(s) == 0:
    print(-1)
else:
    count = 0
    for char in s:
        if char.isalnum():
            count += 1
    print(count)

.
