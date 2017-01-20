import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    data = data.tolist()
    mean = np.mean(data)
    denom_list = [ (i-mean)**2 for i in data ]
    num_list = []
    
    for i in range(len(data)): 
    	num_list.append((data[i]-predictions[i])**2)

    r_squared = 1-np.sum(num_list)/np.sum(denom_list)
   
    return r_squared

    """
The solution on Udacity: 

	SST = ((data-np.mean(data))**2).sum()
	SSReg = ((predictions-data)**2).sum()

	r_squared = 1 - SSReg/SST
    """