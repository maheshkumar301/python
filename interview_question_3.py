#count the small,capital,number,special character
str=input("Enter the word:")
small=0
capital=0
num=0
spec=0
for i in range(0,len(str)):
    if str[i]>='A' and str[i]<='Z':
        capital+=1
    elif str[i]>='a' and str[i]<='z':
        small+=1
    elif str[i]>='0' and str[i]<='9':
        num+=1
    else:
        spec+=1
print("Counts of Capital Letter:",capital)
print("Counts of Small Letter:",small)
print("Counts of numbers:",num)
print("Counts of special character:",spec)

#Count the number digits
numb=int(input("Enter the number:"))
count=0
while numb>0:
    numb=numb//10
    count+=1
print(count)

#Reverse the string
str1=input("Enter a string:")
str2=""
for i in str1:
    str2=i+str2
print(str2)
#check palidrome or not
if (str1 == str2):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")

#Triangle with star
r=int(input("Enter the row:"))
for i in range(1,r+1):
    for j in range(1,r-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print("*",end=" ")
    for j in range(2,i+1):
        print("*",end=" ")
        
    print()

#Sum of number in given digits
n=int(input("Enter a number:"))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n//=10
print("Sum of given digit:",sum)

#Count the each word in string
string=input("Enter a sentence:")
word=input("Enter a word to count:")
words=string.split()
count=0
for w in words:
    if w==word:
        count=count+1
print(count)


    

