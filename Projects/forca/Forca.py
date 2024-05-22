import words
import random as rd

# bugs nao corrigidos 

def err(inEnglish):
    print('No such option!' if inEnglish else 'opção inválida!')
    return None 

def set_idiom():

    print('Idioms:\n'
        'Portuguese (1)\n'
        'English (2)\n')
    
    idiom = None
    while idiom == None:
        try: 
            idiom = int(input('Set idiom (1, 2): '))
            if idiom not in (1, 2): 
                idiom = err(idiom)
            else: 
                return idiom
        except ValueError: 
            idiom = err(idiom)

inEnglish = set_idiom() == 2

def set_diff(inEnglish):

    print(
        'Dificuldades:\n\n'
        'Fácil (a): 7 tentativas\n'
        'Médio (b): 5 tentativas\n'
        'Difícil (c): 3 tentativas\n'
        'Hardcore (d): 1 tentativa\n'
        if inEnglish else
        'Difficulties:\n\n'
        'Easy (a): 7 tries\n'
        'Medium (b): 5 tries\n'
        'Hard (c): 3 tries\n'
        'Hardcore (d): 1 try\n'
    )

    difficulty = None
    while difficulty == None:
        difficulty = input('Select the difficulty (a, b, c, d): ' if inEnglish else 
                           'Selecione a dificuldade (a, b, c, d): ').lower()
        match difficulty:
            case 'a':
                if inEnglish:
                    print('The difficulty was set to -Easy-.' if inEnglish else
                          'A dificuldade escolhida foi -Fácil-.')
                return 7
            case 'b':
                print('The difficulty was set to -Medium-.' if inEnglish else 
                      'A dificuldade escolhida foi -Média-.')
                return 5
            case 'c':
                print('The difficulty was set to -Hard-.' if inEnglish else 
                      'A dificuldade escolhida foi -Difícil-')
                return 3
            case 'd':
                print("The difficulty was set to -Hardcore-.\033[1m You can't fail.\033[0m Good luck! :)" if inEnglish else 
                      'A dificuldade escolhida foi -Hardcore-.\033[1m Você não pode errar.\033[0m Boa sorte! :)')
                return 1
            case _: 
                difficulty = err(inEnglish)

def set_word(inEnglish):
    match inEnglish:
        case False: return rd.choice(words.pt_wlist)
        case True: return rd.choice(words.en_wlist)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

#main func
def game(inEnglish):
    word = set_word(inEnglish)
    tries = set_diff(inEnglish)
    guessed_letters = []
    wrong_guesses = 0
    total_guesses = 0
    best = []

    while tries > 0:

        print('\n', display_word(word, guessed_letters))

        print(f'Remaining tries: {tries}\n' if inEnglish else 
              f'Tentativas faltando: {tries}\n')
        
        letter = input('Type a guess: ' if inEnglish else 
                       'Escreva uma letra: ').lower()
         
        if len(letter) != 1 or not letter.isalpha(): # wrong input
            print('Incorrect input. Type exactly one letter, please.'if inEnglish else 
                  'Entrada incorreta. Escreva exatamente uma letra, por favor.')
        elif letter in guessed_letters: # repeated letter
            print(f'You already guessed that letter! {[letter in guessed_letters]}' if inEnglish else 
                  f'Você já escreveu essa letra! {[letter in guessed_letters]}' )
        elif letter in word: # right letter
            print(f'Nice! The letter {letter.upper()} is in the word!' if inEnglish else
                  f'Boa! A letra {letter.upper()} está na palavra!')
            guessed_letters.append(letter)
        else: # wrong letter
            if tries > 1:
                print(f"Try again... The letter {letter.upper()} isn't in the word." if inEnglish else
                    f"Tente de novo... A letra {letter.upper()} não está na palavra.")
                guessed_letters.append(letter)
                tries -=1
    
        total_guesses += 1

        for wrong_letter in guessed_letters:
            if wrong_letter not in word: 
                wrong_guesses += 1

        if set(word).issubset(set(guessed_letters)): # win message
            best.append(total_guesses)
            print(
                '\n========\n'
                'You Win!\n'
                '========\n'
                f'\nWord: {word}\n'
                f'Wrong Guesses: {wrong_guesses}\n'
                f'Your Best: {min(best)}'

                if inEnglish else

                '\n============\n'
                'Você Ganhou!\n'
                '============\n'
                f'\nPalavra: {word}\n'
                f'Erros: {wrong_guesses}\n'
                f'Recorde: {min(best)}'
            )
            break
    else: # no more tries
        print(f"Your tries are over... The word was {word}.\nDon't worry, you can do better!" if inEnglish else
              f'Suas tentativas acabaram... A palavra era {word}.\nNão se preocupe, você consegue!')
    
# run game
def play(inEnglish):
    game(inEnglish)
    play_again = True
    while play_again == True:
        play_again_input = input('do you want to play again? (y/n) ' if inEnglish else
                                 'Você quer jogar de novo? (y/n) ').lower()
        match play_again_input:
            case 'y': 
                game(inEnglish)
                continue
            case 'n':
                print('thank you for playing!' if inEnglish else
                      'Obrigado por jogar!')
                play_again = False
            case _: print('Please, enter a valid input.' if inEnglish else
                          'Por favor, escreva uma opção válida.')

# execute
play(inEnglish)