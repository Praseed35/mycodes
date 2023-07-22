x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
temp=0
if (y==0 or x==0):
      print(0)
else:      
    for i in range(y):
        temp=temp+x
    print(temp)  
