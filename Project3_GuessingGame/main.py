# # Guessing Game | Rating (9/10)

from random import randint

num_to_guess = randint(1, 10)
lives = 3

while lives > 0:
    try:
        print('Hint: The secret number ranges from 1 to 10.')
        print(f"Lives: {lives}")
        player_guess = int(input("Guess the number: "))
        
        if player_guess < num_to_guess:
            print("Your guess was..Incorrect!")
            print('Hint: Higher.\n')
        elif player_guess > num_to_guess:
            print("Your guess was..Incorrect!")
            print('Hint: Lower.\n')
        else:
            print("Your guess was..Correct!")
            print('You Won!')
            break
            
        lives -= 1
        
        if lives == 0:
            print('Run out of lives... You Lost..')
            print(f'The secret number was.. {num_to_guess}!')
            
    except ValueError as e:
        print("\n---------------------\nInvalid Input!\n---------------------\n")

