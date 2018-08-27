# Question 20 - One edit away

# Write a function to return a boolean that indicates if two strings are one edit away from being identical. The function should take in 2 strings and return a boolean. The definition of an "edit" is as follows:

#     Insert one character
#     Remove one character
#     Replace one character

# A few examples of inputs and the function result are listed below.



#     OneEditAway("pea", "peas") = True


#     OneEditAway("pea", "fleas") = False


#     OneEditAway("pea", "lea") = True


#     OneEditAway("pea", "seas") = False




# Solution will be provided using Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem.

def one_edit_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1 == s2[:j]+s2[j:]:
                return True
            elif s2 = s1[:i]+s1[i:]:
                return True
            elif s1[:i] + s1[i:] == s2[:j] + s2[j:]:
                return True
    return False
