# This is the first code



import string
def printing_words():
    fin = open(r"C:\Users\josep\Desktop\lab-work\book.txt",encoding='utf-8')
    WordList = []
    for line in fin:
        NoWhitespace = line.strip()
        words = NoWhitespace.split()
        for word1 in words:
            word = word1.translate(string.punctuation).lower()
            WordList.append(word)
    print(WordList)

printing_words()
