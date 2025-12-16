# TODO !
from itertools import count
from .utils import Cli

class Auction:
    def __init__(self, cli):
        self.cli = cli
        self.auction_name = "Generic"

    def setup_opening_bid(self) :
        self.cli.display(f'Started auction of type: {self.auction_name}')
        opening_bid = self.cli.prompt('Please enter the amount for the opening bid:')
        opening_bid = int(opening_bid)
        self.cli.display(f"Opening bid is: {opening_bid}")
        return opening_bid

    def setup_bidders(self):
        bidders = []
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
            )
            if not bidder:
                break
            bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")
        return bidders
    
    def announce_winner(self, winner: str | None, standing_bid: int):
        if winner is None:
            self.cli.display("\nNo winner for this auction.")
            return
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {standing_bid}.")

    def auction_loop(self, opening_bid, bidders) :
        raise NotImplementedError("Subclasses must implement this method")
    
    def play(self):
        opening_bid = self.setup_opening_bid()
        winner, standing_bid = self.auction_loop(
            opening_bid,
            self.setup_bidders()
        )

        self.announce_winner(winner, standing_bid)
