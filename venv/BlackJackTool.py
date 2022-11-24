import pandas as pd

#df = pd.read_csv("BlackJackStrat.csv", index_col="DEALER_UP")
df = pd.read_csv("BlackJackStrat.csv",index_col=False)
card_values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}


print("This is designed for online vs computer black jack.")
print("Dealer stands on 17.")

while(True):
    cont_hand = True
    dealer_up = input("Enter dealer up card:\n").upper()
    if dealer_up == 'J' or 'Q' or 'K':
        dealer_up = '10'
    player_cards = input("Enter your cards, seperated by a comma:\n").upper()
    player_card_1,player_card_2 = player_cards.split(',')


    if player_card_2 == 'A' and player_card_1 != 'A':
        player_cards = player_cards[::-1]
        move =  df[(df['DEALER_UP'] == dealer_up)][player_cards].item()

    if player_card_1 != 'A' and player_card_2 != 'A':
        total = card_values.get(player_card_1) + card_values.get(player_card_2)
        if total < 8:
            move = "HIT"
        else:
            move =  df[(df['DEALER_UP'] == dealer_up)][str(total)].item()
    print(move)
    #####

    while(cont_hand):
        next_card = input("Enter next card, or press 'N' for new hand\n").upper()
        if(next_card != 'N'):
            if next_card == 'A' and total < 11:
                total+=11
                move = df[(df['DEALER_UP'] == dealer_up)][str(total)].item()
                print(move)
            elif next_card == 'A' and total > 11:
                total+=1
                move = df[(df['DEALER_UP'] == dealer_up)][str(total)].item()
                print(move)
            else:
                total += card_values.get(next_card)
                if total < 8:
                    move = "HIT"
                    print(move)
                else:
                    move = df[(df['DEALER_UP'] == dealer_up)][str(total)].item()
                    print(move)
        else:
            cont_hand = False













