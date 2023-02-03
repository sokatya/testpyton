a = int(input('ведите первое число: '))
b = int(input('введите второе число: '))
oper = input('ведите операцию (+, -, *, /):')

if oper == '+':
      print (a+b)
elif oper == '-':
    print (a-b)
elif oper == '/' and b!=0:
    print (a/b)
elif oper == '*':
    print (a*b)
else:
    print ('erorr')
