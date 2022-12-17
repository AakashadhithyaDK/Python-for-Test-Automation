num1 = int(input('enter first number'))
num2 = int(input('enter second number'))
choice = int(input('enter choice'))
match(choice):
    case 1 | 5:
        print(num1+num2)
    case 2:
        print(num1 * num2)
    case 3:
        print(num1 - num2)
    case 4:
        print(num1 / num2)
    case other:
        print('enter from 1 to 46')