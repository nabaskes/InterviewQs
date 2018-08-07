# Question 11 - Bias-Variance Tradeoff

# Question: Can you explain the Bias-Variance Tradeoff? Hint: Think about this in the context of learning algorithms and training data.

# Can you share an example where/why you would want to use a biased estimator?

# Upgrade to premium to receive in-depth solutions to each problem.

'''

Basically the bias-variance tradeoff says that the bias of an estimator is
inversely related with the variance of the estimator.  Specifically, if we
have an estimator that predicts very well on the training data (low bias),
it will predict less well on the overall sample.

Basically this is about overfitting.  If you minimize bias too much, you're
likely taking into account random fluctuations in the test data as if they
were real.  If you don't minimize test data enough, you could be missing
important relations

Sometimes a biased relationship is fine.  For instance, if you have a really
messy dataset that you can't pull every relationship from, or if it is a
combination of predictable and unpredictable relations, you can do better than
any alternative by accepting a degree of bias in your data

'''
