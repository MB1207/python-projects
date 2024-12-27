import random

# Define the SlotMachine class
class SlotMachine:
    def __init__(self, balance):
        # Initialize the game with the user's starting balance
        self.balance = balance
        
        # Define the symbols on the slot machine reels
        self.reels = ["🍒", "🍋", "🍊", "🍉", "🍇", "🍓", "🍒", "🍋"]
    
    def display_balance(self):
        # Display the current balance of the user
        print(f"\nYour current balance is: ${self.balance}")
    
    def spin_reels(self):
        # Randomly choose a symbol for each of the 3 reels
        reel_1 = random.choice(self.reels)
        reel_2 = random.choice(self.reels)
        reel_3 = random.choice(self.reels)
        
        # Return the result of the spin (3 symbols)
        return reel_1, reel_2, reel_3

    def calculate_winnings(self, spin_result, bet):
        # Determine the winnings based on matching symbols
        reel_1, reel_2, reel_3 = spin_result
        
        if reel_1 == reel_2 == reel_3:
            # If all three symbols match, calculate the winnings
            if reel_1 == "🍒":
                return bet * 5  # 5x payout for cherries
            elif reel_1 == "🍋":
                return bet * 4  # 4x payout for lemons
            elif reel_1 == "🍊":
                return bet * 3  # 3x payout for oranges
            elif reel_1 == "🍉":
                return bet * 2  # 2x payout for watermelons
            else:
                return bet * 1  # 1x payout for other fruits
        else:
            # If the symbols do not match, no winnings
            return 0

    def play(self):
        # Main game loop. The user can keep playing until they run out of money.
        while self.balance > 0:
            # Show the current balance at the start of each round
            self.display_balance()

            # Get the bet from the user
            try:
                bet = int(input("\nHow much would you like to bet? $"))
                
                # Ensure the bet is positive and does not exceed the balance
                if bet <= 0:
                    print("Your bet must be a positive number. Try again!")
                    continue
                if bet > self.balance:
                    print("You don't have enough balance for that bet. Try a smaller amount.")
                    continue
            except ValueError:
                # If the user enters something that isn't a number, ask again
                print("Please enter a valid number for your bet.")
                continue

            # Deduct the bet from the user's balance
            self.balance -= bet

            # Spin the reels
            spin_result = self.spin_reels()
            print(f"\nSpinning the reels... {spin_result[0]} | {spin_result[1]} | {spin_result[2]}")

            # Calculate the winnings
            winnings = self.calculate_winnings(spin_result, bet)
            self.balance += winnings

            # Show the outcome of the spin and update balance
            if winnings > 0:
                print(f"Congratulations! You won ${winnings}!")
            else:
                print("Sorry, no matching symbols this time. Better luck next spin!")

            # Ask the user if they want to play again or quit
            play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                print("\nThanks for playing! See you next time!")
                break

        # If the user runs out of money, the game ends
        if self.balance <= 0:
            print("\nOh no! You've run out of money. Game over.")

# Main function to start the slot machine game
def main():
    print("Welcome to the Slot Machine! 🎰")

    # Ask the user to set up their starting balance
    try:
        initial_balance = int(input("\nEnter your starting balance: $"))
        
        # Make sure the starting balance is positive
        if initial_balance <= 0:
            print("Starting balance must be greater than zero. Exiting the game.")
            return
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a valid number for the starting balance.")
        return

    # Create an instance of the SlotMachine with the user's starting balance
    slot_machine = SlotMachine(initial_balance)

    # Start the game
    slot_machine.play()

# Entry point of the program
if __name__ == "__main__":
    main()

