#Q1. Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery”


# Count word occurrences in a sentence
string = "To change the overall look of your document. To change the look available in the gallery"

# Remove punctuation and convert to lowercase
import string as str_mod
clean_string = string.replace('.', '').lower()

# Split into words and count occurrences
word_list = clean_string.split()
word_count = {}

for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1

# Print word occurrences
for word, count in word_count.items():
    print(f"{word}: {count}")





    

#Q2. Write a Python program to remove a newline in Python String = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newlines 
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newlines 
clean_string = string.replace('\n', ' ').strip()

print("String without newlines:")
print(clean_string)






#Q3. Write a Python program to reverse words in a string String = “Deeptech Python Training”

# Reverse words in a string
string = "Deeptech Python Training"

# Split the string into words, reverse the order, and join them back
reversed_string = ' '.join(string.split()[::-1])

print("Reversed string:")
print(reversed_string)








#Q4. Write a Python program to count and display the vowels of a given text String=”Welcome to python Training”


# Count and display vowels in a string
string = "Welcome to python Training"
vowels = "aeiouAEIOU"

# Find and count vowels
vowel_list = [char for char in string if char in vowels]
vowel_count = len(vowel_list)

# Display the vowels and their count
print("Vowels found:", ', '.join(vowel_list))
print("Number of vowels:", vowel_count)





