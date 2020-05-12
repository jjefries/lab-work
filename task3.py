# This is third code

import string
file_input=open(r"/content/book.txt", encoding="utf-8")
D={}
E={}
frequency_keys=[]
new_book=[]
new_list=[]
count=0
for line in file_input:
  for word in line.split():
    new_word=word.strip(string.punctuation).lower()
    new_book.append(new_word)
    if new_word not in new_book:
      count=1
      D.update({word:count})
    else:
      count=count+1
      D.update({word:count})
for keys in sorted(D.values(),reverse=True):
  frequency_keys.append(keys)
print(frequency_keys)
# for i in frequency_keys:
#   for val,keys in D.items():
#     if i==keys:
#       E.update({val:keys})
# print(E)
print(len(frequency_keys))
for i in range(len(frequency_keys)):
  new_list.append(i)
print(new_list)

import matplotlib.pyplot as pyplot
pyplot.clf()
pyplot.xlabel("rank")
pyplot.ylabel("frequency")
pyplot.plot(frequency_keys,new_list)
pyplot.show()

def slope():
  x1=max(frequency_keys)
  x2=min(frequency_keys)
  y1=max(new_list)
  y2=min(new_list)
  slope=(y2-y1)/(x2-x1)
  print("The slope of the above graph is:", slope)
slope()
