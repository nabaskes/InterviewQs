# What is Naive Bayes' theorem, and why is it considered 'naive'? Why is it often used in practical applications rather than trying to implement an algorithm based on Bayes' Theorem (non-naive)?

'''

The naive Bayes theorem, also known as the "strong" Bayes theorem, is a special case of the regular Bayes theorem which assumes that the predictors are independent.  Basically, this means that one cannot use one of the variables used to predict the target to predict another one of these.

This is a useful practical assumption to make because prediction becomes harder if the predictor variables can predict each other.  Adding more data wouldn't necessarily be useful, as the data might be redundant.  But in the case of Naive bayes we should be able to train a supervised model without a large amount of data.

Of course, generally speaking, the assumptions are not correct (that is, the prediction variable can predict each other to some extent if they can all predic tthe target variable), so there's something of an upper bound on how effective this sort of model can be
'''
