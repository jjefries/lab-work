# This is the second code

import string
file_name=open(r"C:\Users\josep\Desktop\lab-work\book.txt", encoding="utf-8")
new_book=[]
D={}
first_twenty_keys=[]
first_twenty=[]
different_words=[]
count=0
for line in file_name:
  for word in line.split():
    new_word=word.strip(string.punctuation).lower()
    new_book.append(new_word)
    if new_word not in new_book:
      count=1
      D.update({word:count})
    else:
      count=count+1
      D.update({word:count})

print(new_book)
print("\n")
print("The total number of words in the book are: ", len(new_book))
print("\n")
print("Number of times each word is used: ", D)
print("\n")

for keys in sorted(D.values(),reverse=True)[:20]:
  first_twenty_keys.append(keys)
for i in first_twenty_keys:
  for val,key in D.items():
    if i ==key:
      first_twenty.append(val)
print("The first 20 frequently used words are:",first_twenty)

for key,val in D.items():
  if val==1:
    different_words.append(key)
print("Different words used in the book are:", different_words)
