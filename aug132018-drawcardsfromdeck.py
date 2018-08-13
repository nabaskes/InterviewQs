# Question 15 - Drawing cards from a standard deck

# Suppose we have a standard (52 card) deck of cards. Each card has an equal chance of being one of the four "suits" (e.g. clubs, spades, diamonds, and hearts).

# Question: If you draw 3 cards from the deck, one a time, what is the probability that you draw a club, a heart, and a diamond in that order?

# Upgrade to premium to receive in-depth solutions to each problem.

def prob_club_heart_diamond():
    return (13 / 52) * (13 / 51) * (13 / 50)
