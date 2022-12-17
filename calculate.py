def calculate(number_1,number_2,number_3):
    sum=number_1+number_2+number_3
    difference=number_1-number_2
    product=number_2*number_1
    quotient=0
    try:
        quotient = number_2//number_3
    except ZeroDivisionError:
        print('denominator is 0')
    finally:
        print('Done')
    return sum, difference, product, quotient

'''number_1=int(input('Enter the first number:'))
number_2=int(input('Enter the second number:'))
number_3=int(input('Enter the third number:'))
sum,difference,product,quotient = calculate(number_1,number_2,number_3)
print(sum,difference,product,quotient)'''