"""
Calculate the t and v values for a Welch's t-test using the following equations: 

t = (u1-u2) / ((o1**2/N1)+(o2**2/N2))**0.5

v = ((o1**2/N1)+(o2**2/N2))**2 / ((o1**4/(N1**2*v1))+(o2**4/(N2**2*v2)))
v1 = N1-1
v2 = N2-1

NOTE that we pass in sigma squared (o**2), aka the variance, and not just sigma (o). 
The functions have been modified to reflect this. 
"""

def get_t(u1, u2, o1, o2, N1, N2): 
	numerator = u1-u2 
	denominator = ((o1/N1)+(o2/N2))**0.5

	return numerator/denominator

def get_v(o1, o2, N1, N2): 
	v1 = N1-1
	v2 = N2-1

	numerator = ((o1/N1)+(o2/N2))**2
	denominator = (((o1**2)/((N1**2)*v1))+((o2**2)/((N2**2)*v2)))

	return numerator/denominator


print 'solution, get t: ', get_t(0.299, 0.307, 0.05, 0.08, 150, 165)
print 'solution, get v: ', get_v(0.05, 0.08, 150, 165)