text = input("Enter a sentence: ")
words = text.split()
totalwords = len(words)
print("Total words:", totalwords)

wordcount = {}

for word in words:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1  

most_frequent = max(wordcount, key=wordcount.get)

print("Most frequent word:", most_frequent, "→", wordcount[most_frequent], "times")
