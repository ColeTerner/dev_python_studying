sentence=input("Введите предложение: ")

words=0

for symbol in sentence:
    if symbol==" ":
        words=words+1

sentence=sentence.replace(" ",", ")
print(sentence)
print(words+1)
