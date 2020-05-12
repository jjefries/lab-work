# This is the first code




import string
fin = open(r"C:\Users\josep\Desktop\lab-work\book.txt",encoding='utf-8')
NewBook = []
for line in fin:
  line.strip()
  words=line.split()
  for word1 in words:
      word = word1.translate(string.punctuation).lower()
      NewBook.append(word)
print(NewBook)


# Second method


import string
file_name=open(r"C:\Users\josep\Desktop\lab-work\book.txt", encoding="utf-8")
new_book=[]
for line in file_name:
  for word in line.split():
    new_word=word.strip(string.punctuation).lower()
    new_book.append(new_word)
print(new_book)
