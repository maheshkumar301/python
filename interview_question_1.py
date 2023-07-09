#sum of odd number
sum=0
for i in range(1,101):
    if i%2==1 :
        sum=sum+i
print("Sum of odd number 1 to 100:",sum)

#sum of even number
even_sum=0
for i in range(1,101):
    if i%2==0:
        even_sum+=i
print("Sum of even number 1 to 100:",even_sum)

#count the odd numbers 1to100
odd_count=0
for i in range(1,101):
    if i%2 ==1:
        odd_count+=1
print("Count of oddnumbers 1 to 100:",odd_count)

#count the even number 1 to 100
even_count=0
for i in range(1,101):
    if i%2==0:
        even_count+=1
print("Count of even numbers 1 to 100:",even_count)

#Factorial number
print("**Factorial number***")
f=int(input("Enter the number:"))
if f==0 :
    f=1
    print("***Factorial of given number****",f)
else:
    for j in range(1,f):
        f=f*j
    print("Factorial of given number",f)

#Fibonacci series
print("****FIbonacci Series****")
n=int(input("Enter a number:"))
a=0
b=1
print(a)
print(b)
for i in range(1,n-1):
    n=a+b
    a=b
    b=n
    print(n)

#Find even/odd
print("**Find even/odd**")
e=int(input("Enter a number:"))
if e%2==0 :
    print("The given number is even")
else:
    print("The given number is odd")

#Swapping number using third variable
print("***Swapping number using third variable***")
first_number=int(input("Enter a number:"))
second_number=int(input("Enter a second number:"))
print("Entered number:",first_number,second_number)
temp=first_number
first_number=second_number
second_number=temp
print("After swapping",first_number,second_number)

#Swapping number without using third variable
print("***swapping number without using third variable***")
fir=int(input("Enter a number:"))
sec=int(input("Enter another number:"))
print("Before swapping",fir,sec)
fir=fir+sec
sec=fir-sec
fir=fir-sec
print("After swapping",fir,sec)

#reverse the number
print("***reverse the number***")
r=int(input("Enter a number"))
rev=0
while r>0:
    z=r%10
    rev=(rev*10)+z
    r=r//10
print("Reversed number:",rev)

#to check palindrome number
print("***To check the palindrome number***")
numb=int(input("Enter a number:"))
temp=numb
re=0
while numb>0:
    rem=numb%10
    re=re*10+rem
    numb//=10
print(re)
if re == temp:
    print("The given number is a palindrome")
else:
    print(" The given number is not palindrome")
      
#To print palindrome number 1to 100
print("***To print palindrome number 1to 100***")
for i in range(1,101):
    temp=i
    re=0
    while temp>0:
        rem=temp%10
        re=re*10+rem
        temp//=10
    if re == i:
        print(i,end=" ")
       

#To count the palindrome number 1 to 100
print("\n***To count the palindrome number 1 to 100***")
count_1=0
for l in range(1,101):
    was=l
    res=0
    while was>0:
        rem_1=was%10
        res=res*10+rem_1
        was//=10
    if res==l:
        count_1+=1
print(count_1)

#to check Armstrong number
print("***To check armstrong number***")
arm=int(input("Enter the number:"))
t=arm
n=len(str(t))
cube=0
while arm>0:
    rem=arm%10
    cube=cube+rem**n
    arm//=10
if t==cube:
    print(t,"Armstrong number")
else:
    print(t,"is not Armstrong number")

#To print Armstrong number from 1 to 1000
print("****To print Armstrong number from 1 to 1000****")
for a in range(1,1001):
    cube_n=0
    ty=a
    while a>0:
        rem=a%10
        cube_n+=rem**3
        a//=10
    if cube_n==ty:
        print(ty)

#To count Armstrong number from 1 to 1000
print("@@@@@@@@@@@@To count Armstrong number from 1 to 1000@@@@@@@@@")
count_arm=0
for ar in range(1,1001):
    cube_sum=0
    tr=ar
    while ar>0:
        rema=ar%10
        cube_sum+=rema**3
        ar//=10
    if cube_sum==tr:
        count_arm+=1
print("To count Armstrong number from 1 to 1000:",count_arm)

#Triangle program
t=int(input("Enter the row:"))
for i in range(1,t+1):
    for j in range(i):
        print(end="*")
    print()
for i in range(t+1,1,-1):
    for j in range(i-1):
        print(end="*")
    print()

#To check prime number or not
print("***********To check prime number or not*********")
num=int(input("Enter a number:"))
if num==1:
    print(num,"is not prime number")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            print(num,"is not prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not prime number")

#To print prime number from 1 to 100
print("********To print prime number from 1 to 100**********")
for i in range(1,101):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
            
#To count the prime number from 1 to 100
print("\n***********To count the prime number from 1 to 100************")
count=0
for i in range(1,101):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count+=1
print(count)

#multiplication table
print("********multiplication table****")
multiplicant=int(input("Enter the count:"))
multiplier=int(input("Enter the multiplier:"))
for i in range(1,multiplicant+1):
    print(i,"*",multiplier,"=",i*multiplier)

#biggest four number
k=int(input("Enter first number:"))
l=int(input("Enter second number:"))
m=int(input("Enter third number:"))
n=int(input("Enter fourth number:"))
if k>l and k>m and k>n :
    print("Greatest number is",k)
elif l>m and l>n and l>k:
    print("Greatest number is",l)
elif m>n and m>k and m>l:
    print("Greatest number is",m)
elif n>k and n>l and n>m:
    print("Greatest number is",n)

#To find vowels and non vowels count
str=input("Enter word:")
str=str.lower()
v_count=0
nv_count=0
for i in range(0,len(str)):
        if str[i] in ('a','e','i','o','u'):
            v_count+=1
        elif 'a'<=str[i] and 'Z'<=str[i]:
            nv_count+=1
print("Vowels count",v_count)
print("Non vowels count",nv_count)




