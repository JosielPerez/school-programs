#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 8, 2021
#This program will modify the flood map of new york city.

import numpy as np
import matplotlib.pyplot as plt

#Read in the data to an array, called elevations:
elevations = np.loadtxt('School Programs/20/elevationsNYC.txt')
#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + ( 3, )

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row, col] <= 0:
            #Below sea level
           floodMap[row, col, 0:2] = 1    #Set the water to yellow
        elif elevations[row, col] <= 5:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row, col, 0] = 1     #Set the red channel to 100%
        elif  5 < elevations[row, col,] <= 20:
            floodMap[row, col, :] = .5 #made the rgb color grey
        else:
            #Above the 6 foot storm surge and didn't flood
           floodMap[row, col, 1] = 1 #Set the green channel to 100%

#Load the flood map image into matplotlib.pyplot:
plt.imshow(floodMap)

#Display the plot:
plt.show()

#Save the image:
plt.imsave('floodMap.png', floodMap)