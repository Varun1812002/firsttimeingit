file = open('D:\python5\source\ques1\info.txt', 'r')
data = file.read()
spaces = 0
digits = 0
words = 0
alphabet = 0
for i in data:
    if i == ' ':
        spaces += 1
    elif i.isdigit():
        digits += 1
    elif i.isalpha():
        alphabet += 1
words = spaces + 1
print("Number of Words:", words)
print("Number of alphabet:", alphabet)
print("Number of Digits:", digits)
print("Spaces:", spaces)
file.close()
