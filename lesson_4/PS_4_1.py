from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    data = pandas.read_csv(turnstile_weather)
    plot = ggplot(data, aes(x='ENTRIESn_hourly', y='DATEn'))
    plot + ggtitle('Entries by precipitation') + geom_point(color='purple') + geom_line(color='purple')
    plot.show()
    return plot

plot_weather_data('./turnstile_data_master_with_weather.csv')

'''
, : 0
UNIT, : R001
DATEn, : 2011-05-01
TIMEn, : 01:00:00
Hour, : 1
DESCn, : REGULAR
ENTRIESn_hourly, 
EXITSn_hourly,
maxpressurei, 
maxdewpti, 
mindewpti,
minpressurei, 
meandewpti,
meanpressurei, 
fog, 
rain,
meanwindspdi, 
mintempi,
meantempi, 
maxtempi,
precipi, 
thunder

,0.0,0.0,30.31,42.0,35.0,30.23,39.0,30.27,0.0,0.0,5.0,50.0,60.0,69.0,0.0,0.0

'''

