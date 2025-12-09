# pylint: disable=missing-docstring

from utils import Cli
from itertools import count


class EnglishAuction():

    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()

    def play(self):
        # Input opening bid
        self.cli.display('Started auction of type: English')
        opening_bid = self.cli.prompt('Please enter the amount for the opening bid:')
        opening_bid = int(opening_bid)
        self.cli.display(f"Opening bid is: {opening_bid}")

        # Input bidders
        bidders = []
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
            )
            if not bidder:
                break
            bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")

        # Collect bids
        standing_bid = opening_bid
        winner = None
        pass_count = 0

        while pass_count != len(bidders) :
            pass_count = 0
            for bidder in bidders :
                bid = self.cli.prompt(
                f"Standing bid is {standing_bid}. {bidder} bids:"
            )
                if bid != '':
                    bid = int(bid)
                else :
                    bid = 0
                if bid > standing_bid:
                    standing_bid = bid
                    winner = bidder
                else :
                    pass_count += 1

        # Display winner
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {standing_bid}.")


if __name__ == "__main__":
    auction = EnglishAuction()
    auction.play()
