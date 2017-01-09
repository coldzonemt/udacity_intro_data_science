import numpy
import scipy.stats as stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file by downloading the baseball_stats file from Downloadables below. 
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """
    players = pandas.read_csv(filename)

    players_left = players[players['handedness'] == 'L']['avg']
    players_right = players[players['handedness'] == 'R']['avg']

    t_test=stats.ttest_ind(players_left, players_right, equal_var=False)
    # print t_test
    # If statistical significance is < 95%, then the p value will be <=0.05
    if t_test[1] <= 0.05: 
        pass_test = False
    else: 
        pass_test = True

    statistic = t_test[0]    
    p_value = t_test[1]
    print (pass_test, (statistic, p_value))
    return (pass_test, (statistic, p_value))

compare_averages('./baseball_stats.csv')