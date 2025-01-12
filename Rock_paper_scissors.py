import random

def computer_move():
    random_move = random.choice(['rock','paper','scissors'])
    random_answer = ''
    if random_move == 'rock':
        random_answer ='rock'
    elif random_move == 'paper':
        random_answer = 'paper'
    elif random_move == 'scissors':
        random_answer = 'scissors'
    return random_answer

def user_answer():
    result = ''
    answer = input('Choose rock, paper or scissors: ').strip().lower()
    comparison = computer_move()
    answers= ['You win', 'You loose', 'You draw']
    
    if  answer == 'rock' and comparison == 'rock':
        result = answers[2]
    elif answer == 'rock' and comparison == 'paper':
        result = answers[1]
    elif answer == 'rock' and comparison == 'scissors':
        result = answers[0]
    elif answer == 'paper' and comparison == 'rock':
        result = answers[0]
    elif answer == 'paper' and comparison == 'paper':
        result = answers[2]
    elif answer == 'paper' and comparison == 'scissors':
        result = answers[1]
    elif answer == 'scissors' and comparison == 'rock':
        result = answers[1]
    elif answer == 'scissors' and comparison == 'paper':
        result = answers[0]
    elif answer == 'scissors' and comparison == 'scissors':
        result = answers[2]
    return result.title()
    #f'You picked {answer.title()}. Computer picked {comparison.title()}.

user_answer()
'''wins= 0
loses=  0
draws=  0

if user_answer() == 'You win':
    wins+=1
elif user_answer == 'You loose':
    loses+=1
elif user_answer() == 'You draw':
    draws+=1

with open('rcp_results.txt', 'w') as rcp_file:
    rcp_file.write(wins)'''

    