print('\n\nHello world!')
print('Welcome to my game of blackjack!\n\n')
print('D = Diamonds, S = Spades, H = Hearts, C = Clubs')
bank = 10
play = True
print('You have: ' + str(bank) + ' credits\n\n')
while play:
    handvalue = 0
    first = True # checks whether it's the user's first move of the hand
    ucont = True # checks whether or not the user keeps going
    wager = input('How much would you like to wager? :')
    if int(wager) > bank:
        print('\nYour wager cannot be more than your bank.\n')
        continue
    # create deck
    # shuffle deck
    # create user hand
    # create dealer hand (with one card)
    # check for blackjack hand
    # display output
    while ucont:
        if first:
            choice = input('\nHit, Stay, or Double?\n')
            if choice == 'Hit': # this if and these elifs need fixed
                print('\nOkay.')
                bank = bank - 10
                break
            elif choice == 'Stay':
                print('\nYou got it, champ.')
                bank = bank - 10
                break
            elif choice == 'Double':
                if int(wager) * 2 <= bank:
                    print('\nSure, why not.')
                    bank = bank - 10
                    break
                else:
                    print("\nYou can't do that.")
                    bank = bank - 10
                    break
            else:
                print('\nInvalid Selection')
                continue
        # whether hit, stay, or double (if first time)
        print("\nYour hand's current value is: " + str(handvalue) + '\n')
        if handvalue > 21:
            ucont = False
        first = False
    # deal for computer using dealer rules
    # evaluation of which is higher, if dealer busts
    # display output
    if bank == 0:
        play = False
    if play == False:
        break# play again?
if bank == 0:
    print('\nGame over. You lost.')
elif bank <= 10:
    print("\nYour final score was ' + int(bank) + '. At least you didn't lose.")
else:
    print('\nYour final score was ' + int(bank) + '. Nice!')