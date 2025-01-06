try:
    first = float(input('First: '))
    operator = input('Operator: ')
    second = float(input('Second: '))
    sum = first + second
    sum_2 = first - second
    sum_3 = first * second
    sum_4 = first / second
    sum_5 = first ** second

    if operator == '+':
        print(f'Sum:{sum:.2f}')
    elif operator == '-':
        print(f'Sum:{sum_2:.2f}')
    elif operator == '*':
        print(f'Sum:{sum_3:.2f}')
    elif operator == '/':
        print(f'Sum:{sum_4:.2f}')
    elif operator == '**':
        print(f'Sum:{sum_5:.2f}')
    else:
        print('Invalid operator')
except ValueError as error:
    print(error)

""" python cant conactinate float() and str(). so to solve this problem in this case. make another variable adding the two floats toghether and then when concatinating them convert the sum variable into a string so that it works.
python can only concatiante like data types: str() with str() and so on 
you can convert a value either by input of later"""
