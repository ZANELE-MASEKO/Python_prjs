password= ''

while len(password) <10:
    if len(password) < 10:
        password= input('->Password has to be 10 letter or more.\n->Password needs to contain number/s.\nEnter password:').strip()
    elif len(password) >= 10:
        password= password

name= input('Enter your name?')
surname= input('Enter your surname?')
birth= input('enter your birth year')

name_3= name[:3].upper()
surname_3= surname[:3].upper()
birthyear= birth[2:]
username = f'{name_3}{surname_3}@{birthyear}'

print(f'Username is: {username}')
print(f'Your password is: {password}')