
dividend=int(input("Enter a dividend number:"))
divisor=int(input("Enter a divisor number:"))
sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
if(divisor==0):
      print("invalid input")
dividend = abs(dividend)
divisor = abs(divisor)
temp=0
while (dividend >= divisor):
        dividend = dividend-divisor
        temp = temp+ 1
        if sign == -1:
            temp = -temp
            break
 
print(temp)