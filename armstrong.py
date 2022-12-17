num1 = int(input('enter a number'))
backup = num1
sum=0
while (num1 > 0):
     r=num1 % 10
     print(r)
     sum += r * r * r
     print(sum)
     num1//=10
     print(num1)
if (sum == backup):
 print('armstrong num')
else:
    print('not a armstrong number')
