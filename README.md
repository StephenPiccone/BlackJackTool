# BlackJack Strategy Tool

This is a tool designed to provide the user with the best move in their current situation. The BlackJackStrat.csv file contains moves for every possible situation, and can be edited if a user wishes to adjust their strategy.

## Game Loop

The tool requires input from the user in order to provide advice for their best move. The tool asks the user for the card the dealer is showing, as well as the cards in the users hand. With this information, the tool references the strategy sheet and provides the user with the best move as indicated on the sheet.

Example hand of dealer and user
![blackjack-start](/blackjack-start.png)

The user then has the option to either start a new hand by inputting "N", or input the next card they recieved. If the user chooses to input another card, it's value is added to the users total and a new move is suggested from the strategy sheet based on the users updated total.

User inputs new card
![blackjack-nextcard](/blackjack-nextcard.png)