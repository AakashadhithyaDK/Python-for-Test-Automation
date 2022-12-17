'''ans=lambda x : x + 3
print(ans(3))

sum=lambda num1,num2 : num1+num2
print(sum(10,20))
'''
def add(num2):
    return lambda num1 : num1+num2

addition=add(3)
print(addition(5))