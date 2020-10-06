#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
people=['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
word1=(input("Enter word from list")).strip()
word2=(input("Enter another word")).stip()
x=people.index(word1)
x=int(x)
people.insert(x,word2)
people.remove(word1)
print(people)
