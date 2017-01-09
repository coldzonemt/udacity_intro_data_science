import numpy
from pandas import DataFrame, Series


def numpy_dot():
    '''
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each 
    bronze medal.  

    Using the numpy.dot function, create a new dataframe called 
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.
           
    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
 
    # YOUR CODE HERE
    gold_points = [medal*4 for medal in gold]
    silver_points = [medal*2 for medal in silver]
    bronze_points = [medal*1 for medal in bronze] #unnecessary; for illustration only. 
    
    gold_dot = numpy.dot(gold, 4)
    silver_dot = numpy.dot(silver, 2)
    bronze_dot = numpy.dot(bronze, 1)

    print gold_dot
    print silver_dot
    print bronze_dot

    total_points = numpy.add(gold_dot, silver_dot)
    total_points = numpy.add(total_points, bronze_dot)

    print total_points

    olympic_points_df = DataFrame({'country_name':countries, 'points': total_points})
    print olympic_points_df

    # Or, from the solution: 
    df['points'] = df[['gold','silver','bronze']].dot([4, 2, 1]) olympic_points_df = df[['country_name','points']]

    return olympic_points_df

numpy_dot()