from random import *
print( 'Hangman ')
words= 'ant bat cat rat mat are orb new net not'.split()
def andword():
    a = randint(0,len(words)-1)
    return words[a]
secretword= andword()
length= len(secretword)
blanks= '_'
blanks= blanks*length
incorrect_choices=0
ctr=0
correct=''
incorrect=''
def checkguess(g,blanks,ctr,incorrect,correct,incorrect_choices):
    for i in secretword:
        if g in correct or g in incorrect:
            print('You have tried this letter earlier')
            break
        elif g==i:
            print('Correct Guess')
            correct=correct+g
            blanks= blanks[:ctr]+g+blanks[ctr+1:]
            break
        ctr=ctr+1
    if g not in secretword and g not in incorrect:
        print('Incorrect Guess')
        incorrect=incorrect+g
        incorrect_choices=incorrect_choices+1
    print(HANGMAN[incorrect_choices])
    return (blanks,incorrect,correct,incorrect_choices)
            
            
    
HANGMAN= [''' '''
          ,'''
   0   ''','''
   0
   |   ''','''
   0
  /|   ''','''
   0
  /|\  ''','''
   0
  /|\   
  /    ''','''
   0
  /|\   
  / \   ''']
blank='_'

while True:
    if '_' in blanks:
        g=input('Enter a guess ')
        (blanks,incorrect,correct,incorrect_choices)=checkguess(g,blanks,ctr,incorrect,correct,incorrect_choices)
        print(blanks)
        if incorrect_choices>5 or blanks== secretword:
            if incorrect_choices>5:
                print('Game Over..... The word was...', secretword)
            else:
                print('Awesome, you did it!!!!')
            print('Do you wanna try again? (y or n)')
            ans=input()
            if ans=='y':
                print ("\n" * 50)
                secretword= andword()
                length= len(secretword)
                blanks= '_'
                blanks= blanks*length
                incorrect_choices=0
                ctr=0
                correct=''
                incorrect=''
            else:
                break
            


    


   
