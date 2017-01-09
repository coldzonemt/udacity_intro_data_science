import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    #Assume you will be reading in a csv file with the same columns that the
    #Lahman baseball data set has -- most importantly, there are columns
    #called 'nameFirst' and 'nameLast'.
    #1) Write a function that reads a csv
    #located at "path_to_csv" into a pandas dataframe and adds a new column
    #called 'nameFull' with a player's full name.
    #
    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron', 
	#
	#2) Write the data in the pandas dataFrame to a new csv file located at
	#path_to_new_csv
    baseball_data = pandas.read_csv(path_to_csv)
    # print baseball_data

    baseball_data['nameFull'] = baseball_data['nameFirst'] + ' ' + baseball_data['nameLast']
    print baseball_data['nameFull']

    baseball_data.to_csv(path_to_new_csv)


path_to_csv = "./baseballdatabank-master/core/Master.csv"
path_to_new_csv = "new_baseball_master.csv"
add_full_name(path_to_csv, path_to_new_csv)