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

    clf_after_cleaned =linear_model.LinerRegression()
    cleaned_d = outlierCleaner(reg.predict(ages_train),ages_train,net_worths_train)
    ages_cleaned = numpy.array([e[0]for e in cleaned_d])
    net_worths_cleaned = numpy.array([e[1]for e in cleaned_d])
    clf_after_cleaned.fit(age_cleaned,net_worths_cleaned)

    return cleaned_data
    print clf_after_cleaned.coef_
