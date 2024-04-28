from funcs_for_challenge import generate_problem, check_guess, TOTAL_PROBLEMS
import time

def play_game():
    start_time = time.time()
    input('Press enter to start')
    print('---------------------')

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        check_guess(answer, i+1, expr)

    end = time.time()
    total_time = round(end - start_time, 2)
    print('---------------------')
    print(f'Nice work! You finished in {total_time} seconds!')

if __name__ == '__main__':
    play_game()