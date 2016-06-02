#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = abs(predictions - net_worths)
    max_index = error.argsort(axis=0)[-10:]
    
    for i in range(len(ages)):
        if i not in max_index:
            cleaned_data.append((ages[i], net_worths[i], error[i]))

    

    return cleaned_data

