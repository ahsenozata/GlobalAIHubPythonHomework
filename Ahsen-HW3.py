import random
name = input("What is your name? ")
print("Welcome", name,"!")
words = ['cupcake', 'coffee', 'environment', 'star',
         'rubbish', 'Turkish', 'flower' , 'hour',
         'board', 'lemon', 'project', 'competition']
word = random.choice(words)
print("Guess the letter")
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for i in word:
        if i in guesses:
            print(i)

        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You are Winner")
        print("The word is: ", word)
        break
    guess = input("guess a letter:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Fail!")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You are Looser")