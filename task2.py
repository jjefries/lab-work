# This is the second code

import string
fin = open(r"C:\Users\josep\Desktop\lab-work\book.txt",encoding='utf-8')
NewBook = []
D={}
count=0
for line in fin:
  line.strip()
  words=line.split()
  for word1 in words:
      word = word1.translate(string.punctuation).lower()
      NewBook.append(word)

      if word not in NewBook:
          count=1
          D.update({word: count})
      else:
          count+=1
          D.update({word: count})
print(NewBook)
print(len(NewBook))
print(D)
print(sorted(D.values()))
