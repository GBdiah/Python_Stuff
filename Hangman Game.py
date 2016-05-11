'''HANGMAN GAME IN PYTHON
SUBJECT: ALGORITHM E PROGRAMING
TEACHER.: CARLOS EDUARDO
GROUP: GABRIEL DA SILVA COSTA VASCONCELOS DE ARAÚJO 
ALECSANDER DANIEL CRUZ  
CAIO MARTINS LEMOS DE SOUZA '''
import sys
import string # manipulate the words on the list
import random # to choose a word

easy_list = ['better', 'large', 'light', 'blue', 'red', 'black', 'white', 'house', 'time', 'hapiness', 'kindness', 'life',
'pencil', 'horse', 'train', 'hit', 'cosmos']

hard_list = ['procrastinate', 'autority', 'discussion', 'doutrination', 'dwarves', 'luxury', 'nowadays',
'numbskull', 'unworthy', 'unknown', 'xylophone', 'yachtsman', 'wyvern', 'jukebox', 'iatrogenic']
E_= True
H_= False
dificulty = True

exit = False

while (not exit):
    print ("---------------------------")
    print ("        HANGMAN GAME       ")
    print ("       only low case       ")
    print ("---------------------------")
    print ("1- START MATCH         ")
    print ("2- DIFICULTY  ")
    print ("3- EXIT")
    
    while True:
        option = input('SELECTED OPTION: ')
        print()

        if (option == '1') or (option == '2') or (option == '3'):
            break

            print('SORRY, THAT IS NOT A VALID OPTION')

    if option == '3':
        exit = True
#--------------DIFICULTY MENU---------------------------------- #       
    if option == '2':
        back = False
        while (not back):
            
           #--------------The little "*"-----------#
            
            if E_ == True:
                EE = '*'
            else:
                EE = ''
            if H_ == True:
                HH = '*'
            else:
                HH = ' '
#------------------------------------------------------------------#
                
            print ('---------------------------')
            print ('        HANGMAN GAME       ')
            print ('---------------------------')
            print ('E- EASY',EE)
            print ('H- HARD', HH)
            print ('')
            print ('B- BACK')
            while True:
                dific = input('OPTION: ')
                print()
                if (dific == 'E') or (dific == 'H') or (dific == 'B'):
                    break

                print ('SORRY, THAT IS NOT A VALID OPTION')

            if dific == 'B':
                back = True

            if dific == 'E':
                E_ = True
                H_ = False
                dificulty = True #True is EASY

            if dific == 'H':
                E_ = False
                H_ = True
                dificulty = False #False is HARD
            
#-----------------------------GAME CONDITIONS-----------------------------        
    if option == '1':
        if dificulty == True:
            list_ = easy_list
            lives = 5
        elif dificulty == False:
            list_ = hard_list
            lives = 3
    
#--------------------------- STARTING THE GAME---------------------------------
        joao = lives
        game_complete = False
        wrong_letters = []
        correct_letters = []
        used_letters = []
        word = list_[random.randint(0,len(list_)-1)]
        blanks = '_' * len(word)
        while game_complete == False:

            print('Already used letters: ', end=' ') # print das letras utilizadas
            for i in range(0, len(used_letters)):
                print(used_letters[i], end=' ')
            print(end='\n\n')
 
            
            for i in range(len(word)): # print dos underlines e das letras corretas
                if word[i] in correct_letters:
                    blanks = blanks[:i] + word[i] + blanks[i+1:]
            print('Word: ', end=' ')
            for letter in blanks:
                print(letter, end=' ')
            print(end='\n\n')

            print ('Type a letter (0 to exit).', (joao-len(wrong_letters)), 'attempts remaining.')
            guess = input ('> ')
            print()
            
            while guess in used_letters:
                print ("Letter '",guess ,"' already used. Try another one.", sep='', end='\n\n')
                print ('Type a letter (0 to exit).', (joao-len(wrong_letters)), 'attempts remaining.')
                guess = input ('> ')
                print()
              
            
              
            if guess == '0':
                break

            if len(guess)!= 1:
                print ('Hm? That is not a letter son.', end='\n\n')
                joao = 1
            elif guess in wrong_letters:
                print ("Letter '",guess ,"' already used. Try another one.", sep='', end='\n\n')
            elif guess not in 'abcdefghijklmnopqrstuvwxyzçôóõíé':
                print ('Hm? That is not a letter son!', end='\n\n')
                joao = 1
            elif guess in used_letters:
                print ("Letter '",guess ,"' already used. Try another one.", sep='', end='\n\n')
            else:
                used_letters.append(guess)
                if guess in word: # Letters verification in the word
                    print("Sweet! The letter '", guess, "' exist :)", sep='', end='\n\n')
                    correct_letters.append(guess)
                    
                    complete_word = True # verify if the player won the game
                    for (i) in range (len(word)):
                        if word[i] not in correct_letters:
                            complete_word = False
                            break
                    if complete_word:
                        print("Congratulations! You won the game. The word was '", word, "'.", sep='')
                        print ("Press enter to continue...", end='\n\n')
                        game_complete = True
                            
            if guess not in correct_letters: #used letters
                if guess in 'abcdefghijklmnopqrstuvwxyzçôóõíé': 
                    if guess not in wrong_letters:
                        print("Letter '", guess,"' does not exist in the word :(", sep='', end='\n\n')
                        wrong_letters.append(guess)
                        
            if len(wrong_letters) == joao :
                print ("GAME OVER. The word was '", word,"'.", sep='')
                print ("Press enter to continue...", end='\n\n')
                game_complete = True
                
            if game_complete:
                play_again = input ('')
                print()
                if play_again == (''):
                    game_complete = False
                    joao = lives
                    wrong_letters = []
                    correct_letters = []
                    used_letters = []
                    word = list_[random.randint(0,len(list_)-1)]
                    blanks = '_' * len(word)
                else:
                    break
