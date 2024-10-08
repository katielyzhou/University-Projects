import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

file = 'FILEHERE.txt'

# Gaussian assumes there is 0 offset.
# w = std dev, width
# A = scale factor
# x0 = centre

#Red starting parameters
w1 = 1
A1 = 30000
x01 = 650

#Green starting parameters
w2 = 5
A2 = 40000
x02 = 520

#Blue starting parameters
w3 = 5
A3 = 50000
x03 = 450

#Defining functions for plotting one gaussian and the sum of all three.
def gaussian1(x,w,A,lambda_0):
    return A*np.exp(-(x - lambda_0)**2/(2*w**2))

def gaussian3(x,w1,A1,x01, w2, A2, x02, w3, A3, x03):
    return A1*np.exp(-(x - x01)**2/(2*w1**2)) + A2*np.exp(-(x - x02)**2/(2*w2**2)) + A3*np.exp(-(x - x03)**2/(2*w3**2))

#open file
signal=open(file,'r')

#start reading the file to find out how many lines to skip
#data is required to have the below line else code will hang.
startdata='>>>>>Begin Processed Spectral Data<<<<<'
line = 1
readline = True
while readline:
    linedata=signal.readline()
    linedata=linedata.strip()
    if linedata == startdata:
        readline = False
    else:
        line = line + 1
signal.close()

data=np.genfromtxt(file,skip_header=line,skip_footer=1)
xdata = data[:,0]
ydata = data[:,1]
npts = len(xdata)

#fitting
popt, pcov = curve_fit(gaussian3,xdata,ydata,p0=[w1,A1,x01, w2, A2, x02, w3, A3, x03])
pars_1 = popt[0:3] #Parameters for the first Gaussian
pars_2 = popt[3:6]
pars_3 = popt[6:9]
gauss_red = gaussian1(xdata, *pars_1) #Gaussian plot (y values)
gauss_green = gaussian1(xdata, *pars_2)
gauss_blue = gaussian1(xdata, *pars_3)

G = np.empty((npts))
for i in range(npts):
        G[i] = gaussian3(xdata[i], *popt)

#Plotting
plt.figure()
plt.plot(xdata,ydata, label ="Experimental")        
plt.plot(xdata,G, label="Fit")
plt.xlim(400,750)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")
plt.legend()

#Plot individual Gaussians
plt.plot(xdata, gauss_red, color='red')
plt.plot(xdata, gauss_green, color='green')
plt.plot(xdata, gauss_blue, color ='blue')

#Intensities of the individual gaussians
I_r = gaussian1(popt[2], *pars_1)
I_g = gaussian1(popt[5], *pars_2)
I_b = gaussian1(popt[8], *pars_3)
print("Red intensity:", I_r)
print("Green intensity:", I_g)
print("Blue intensity:", I_b)
