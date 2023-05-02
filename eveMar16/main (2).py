word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
# Print the word assigned to word_without_vowels.
user_word = input("Enter a string = ")
user_word = user_word.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter in "AEIOU":
        continue
    else:
        word_without_vowels+=letter
        
print(word_without_vowels)

