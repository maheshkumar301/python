#Binary search
l=[]
s=int(input("Enter the size of list:"))
for i in range(1,s+1):
    a=int(input("Enter the elements:"))
    l.append(a)
print(l)
for i in range(1,s):
    for j in range(i+1):
        if l[i]<l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
search=int(input("Enter a searching element:"))
f=0
la=len(l)-1
mid=0
while f<la:
    mid=(f+la)//2
    if search == l[mid]:
         break
    elif search< l[mid]:
        la=mid-1
    else:
        f=mid+1


print(mid)
    
    
