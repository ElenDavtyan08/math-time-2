import random
OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + str(operator) + ' ' + str(right)
    answer = eval(expr)
    return expr, answer

def check_guess(answer, problem_number, expr):
    while True:
        guess = input('Problem #' + str(problem_number) + ': ' + expr + ' = ')
        if guess == str(answer):
             break