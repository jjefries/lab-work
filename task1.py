# This is the first code
import string
print(string.punctuation)
f_input=open("books.txt")
Lst1=[]
for line in f_input():
    word=NoWhitespace.split()
    for word1 in word:
      word=word1.translate(string.punctuation).lower()
      Lst1=Lst1+[word]
    print(Lst1)

