#Ascending order using list
list=[]
size=int(input("Enter size of list:"))
for i in range(1,size+1):
    ele=int(input("Enter the elements:"))
    list.append(ele)
print(list)
for i in range(len(list)):
    for j in range(i+1):
        if list[i]<list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print("Ascending order of list:",list)

#Descending order using list
list_1=[]
size_1=int(input("Enter the size of list:"))
for i in range(1,size_1+1):
        ele_1=int(input("Enter the elements:"))
        list_1.append(ele_1)
print(list_1)
for i in range(len(list_1)):
    for j in range(i+1):
        if list_1[i]>list_1[j]:
            temp=list_1[i]
            list_1[i]=list_1[j]
            list_1[j]=temp
print("Descending order of list_1:",list_1)
            
#second minimum number
print("Second minimum number of list:",list[1])
#first maximum number
print("First maximum number of list:",list[-1])
#third maximum number
print("Third maximum number of list:",list[-3])
    
