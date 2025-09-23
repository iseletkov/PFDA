words = 'Ехали медведи на велосипеде'



[word for word in words.split() if len([c for c in word.lower() if c in "aeiouyаяуюоёэеиы"]) >= 3]
print(result)