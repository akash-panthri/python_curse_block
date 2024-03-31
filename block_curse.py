word = ['shit','curse','name']
text = open("requ.txt","r").read().split()

for i in text:
    if i in word:
        text[text.index(i)] = len(i)*'*'
ten =  " ".join(text)
print(ten)

