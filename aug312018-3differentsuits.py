
# Question 23 - Drawing cards from a standard deck, once more

# Suppose we have a standard (52 card) deck of cards, with an equal share of the cards associated with each of the four "suits" (e.g. clubs, spades, diamonds, and hearts). You can read more about a standard card deck here.

# Question: If you were to draw 3 cards from the deck, one a time, what is the probability that you draw a club, a heart and a diamond in any order? Be sure you can explain your reasoning here using probablity theory.


'''
This is a pretty simple question.

You are doing three separate events.  The first one is a "hit" so long as
you don't draw a spade.  1/4 of cards are spades, so this is a hit 3/4 of the
time.

Now, this differs a bit as to whether we are replacing pulled cards.  First,
with replacement

The second one is a hit whenever you don't draw a spade, or whatever suit
you drew the previous step.  This eliminates half of all cards, so you have
a 1/2 hit chance here.

The final pull, you must not pull a spade or either of the two suits seen before.  That is, you must pull the unseen non-spade suit.  This is only 1/4 of cards.

All aggregated, you have a 3/4 * 1/2 * 1/4 = 3 / 32 chance of succeeding...

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With replacement, the numbers are uglier, but your odds improve slightly, as you decrease the number of different suit cards each time.  The principles are the same.

The first pull is still 3/4.
The second pull, though, has a slightly smaller deck, so this is 26/51, which is slightly better than 1/2
The third pull is 13/50, which is again slightly better than 1/4.

Ergo, the odds are 3/4 * 26/51 * 13/50 = 1014 / 10200 = 507 / 5100 = 169/1700

169/1700 ~= 0.099, and 0.09375.  So, the odds without replacement is about 2/3 of a percent better
