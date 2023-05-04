import random
import os
draw = True
play = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []
def deck_clear():
    your_cards.clear()
    computer_cards.clear()     
while play:
    new_game = input("press 'y' to start game, press 'n' to exit: ")
    draw = True
    if new_game == 'y':
        os.system('cls')
        for card in range(2):
            number = random.choice(cards)
            your_cards.append(number)
            if card == 1:
                score = sum(your_cards)
                print(your_cards)
                print(f"That's your {score} score")
        for card in range(2):
            number = random.choice(cards)
            computer_cards.append(number)
            if card == 0:
                print (f"That's computer first card: {computer_cards}")
            elif card == 1:
                score_computer = sum(computer_cards)
                while score_computer != 0 and score_computer < 17:
                    number = random.choice(cards)
                    computer_cards.append(number)
                    score_computer = sum(computer_cards)
            
        while draw:
            next_card = input("press 'y' to draw new card, press 'n' to stick with your hand: ")
            if next_card == 'y':
                for card in range(1):
                    number = random.choice(cards)
                    your_cards.append(number)
                if card == 0:
                    score += number
                    print(your_cards)
                    print(f"That's your {score} score")
            else:
                if score > score_computer:
                    draw = False
                    if score > 21 and score_computer > 21:
                        if score > score_computer:
                            draw = False
                            os.system('cls')
                            print("You won")
                            print(f"That's your {score} score")
                            print(your_cards)
                            print(f"That's computer {score_computer} score")
                            print(computer_cards)
                            deck_clear() 
                        elif score_computer > score:
                            draw = False
                            os.system('cls')
                            print("Computer won")
                            print(f"That's your {score} score")
                            print(your_cards)
                            print(f"That's computer {score_computer} score")
                            print(computer_cards)
                            deck_clear() 
                        elif score_computer == score:
                            draw = False
                            os.system('cls')
                            print("It's a draw")
                            print(f"That's your {score} score")
                            print(your_cards)
                            print(f"That's computer {score_computer} score")
                            print(computer_cards)
                            deck_clear()   
                    os.system('cls')
                    print("You won")
                    print(f"That's your {score} score")
                    print(your_cards)
                    print(f"That's computer {score_computer} score")
                    print(computer_cards)
                    deck_clear()    
                elif score < score_computer:
                    if 21 < score_computer:
                        draw = False
                        os.system('cls')
                        print("You won, computer went over")
                        print(f"That's your {score} score")
                        print(your_cards)
                        print(f"That's computer {score_computer} score")
                        print(computer_cards)
                        deck_clear()
                    else: 
                        draw = False
                        os.system('cls')
                        print("Computer won")
                        print(f"That's your {score} score")
                        print(your_cards)
                        print(f"That's computer {score_computer} score")
                        print(computer_cards)
                        deck_clear()     
                else:
                    draw = False
                    os.system('cls')
                    print("It's a draw")
                    print(f"That's your {score} score")
                    print(your_cards)
                    print(f"That's computer {score_computer} score")
                    print(computer_cards)
                    deck_clear()   
    elif new_game == 'n':
        print("See you")
        play = False
    else:
        os.system('cls')
        print("press right key")
        new_game = input("press 'y' to start game, press 'n' to exit: ")
        play = True
