file2=open('D:\python5\source\ques2\word.txt','w')
file3=open('D:\python5\source\ques2\\vowel.txt','w')
file4=open('D:\python5\source\ques2\digit.txt','w')
file1=open("D:\python5\source\ques2\\abc.txt",'w+')
a=input("Enter the line:")
file1.write(a)
file1 = open("D:\python5\source\ques2\\abc.txt", 'r')
data = file1.readline()
for i in data:
    if i.isalpha():
        file2.write(i)
        file2.write("\n")
    elif i.isdigit():
        file4.write(i)
for i in data:
    for ch in i:
        if ch in ['a','e','i','o','u','A','E','I','O','U']:
            file3.write(i)
            file3.write("\n")
file2.close()
file3.close()
file4.close()
