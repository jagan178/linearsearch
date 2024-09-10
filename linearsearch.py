flag=-1
arr=[]
n=int(input("enter the size of elements:"))
for i in range(n):
    data=int(input("Enter the elements:"))
    arr.append(data)
search=int(input("Enter the search element:"))
for i in range(n):
    if arr[i]==search:
        flag=i
        break
if(flag==-1):
    print("element not found")
else:
    print(f"element present at index {flag} ")
 
