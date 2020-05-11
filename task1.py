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
