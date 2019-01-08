# Question 76 - Resampling

# Can you explain what resampling is? Can you name 2 seperate resampling methods and explain the pros and cons?

# Bonus: Can you tell me about a time where you had to use a resampling technique?

# Upgrade to premium to receive in-depth solutions to each problem.

'''

Resampling is a class of methods that repeatedly take samples out of a dataset in order to construct new datasets for some reason or another.

One common type of resampling is boostrapping, which uses sampling with replacement repeatedly on a dataset.  We repeatedly sample the original dataset to get new datasets, and record the mean of the new dataset.  The resulting set of means should have a gaussian distribution, which is nicer to work with.  Assuming the underlying population is normally distributed, which it probably is if it is large enough, than we have recreated some similacrum of the original dataset.

A main benefit of bootstrapping is that it is simple and easy to understand.  This makes it a very good technique for exploratory data analysis.  However, it's a chainsaw approach and can miss certain things.  For instance, depending on the sample, we may miss important tail features of the original dataset.  Further, since boostrapping assumes independence, if the underlying data isn't independent, we won't conclude anything real.


Another type of resampling is cross-validation, which is a frequent part of the data science process whenever our dataset is large enough that bootstrapping isn't needed.  This consists of randomly dividing up our dataset into two groups: a training group and a testing group.  This is conveniently done with train_test_split() from sklearn.  The model is trained on the training group, and the testing group is used to make sure it works properly.  This helps to determine whether the model is overfit, and a number of cool comparisons can be made, such as comparing the accuracy of the trained model when applied on training versus testing data.  We usually want to do this while determining the type of model used.


I've done each of these things pretty frequently
'''
