from datetime import datetime

def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    Hint: 
    There are a couple of useful functions in the datetime library that will
    help on this assignment, called strptime and strftime. 
    More info can be seen here and further in the documentation section:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''

    #input: month-day-year (2 digit year)
    #output: year-month-day (4 digit year)
    d_fmt = datetime.strptime(date, '%m-%d-%y')
    date_formatted = d_fmt.strftime('%y-%m-%d')
    if len(date_formatted.split('-')[0]) == 2: 
        date_formatted = '20'+date_formatted
    return date_formatted


# date_input = datetime.now()
# print 'input:', date_input
# print type(date_input)
reformat_subway_dates('05-01-11')
# reformat_subway_dates(date_input)