
# Modify the previous program to read a word list and then print all the words in the book that are not in the word list. How many of them are typos? How many of them are common words that should be in the word list, and how many of them are obscure?
# Python provides a data structure called set that provides many common set operations. Read the documentation and write a program that uses set subtraction to find words in the book that are not in the word list.

import string
my_word_list=["hello", "my", "dear", "students", "today"]
book_list=[]
f_input=open(r"C:\Users\josep\Desktop\lab-work\book.txt",encoding='utf-8')
for line in f_input:
  line.strip()
  words=line.split()
  for word in words:
    op=word.translate(string.punctuation).lower()
    book_list.append(op)
first_set=set(my_word_list)
second_set=set(book_list)
print(first_set.difference(second_set))
