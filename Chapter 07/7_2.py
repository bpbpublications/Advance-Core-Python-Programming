#7.2.2 Plotting a point

#import pyplot
import matplotlib.pyplot as plt

#define the values of x and y
x = 5
y = 8

#plot the point with the help of plot(x,y) function
plt.plot(x,y)

#display the plot
plt.show()
######################################################3

#import pyplot
import matplotlib.pyplot as plt

#define the values of x and y
x = 5
y = 8

#plot the point with the help of plot(x,y) function, red color, marker style X
plt.plot(x,y,'rx')

#display the plot
plt.show()
##########################################################

#import pyplot
import matplotlib.pyplot as plt

#plot the point with the help of plot(5,8) function, cyan color, marker style hexagon
plt.plot(5,8,'ch')

#display the plot
plt.show()
#############################################################

#import the pyplot module from matplotib library
import matplotlib.pyplot as plt

#define two lists for the values of x and y 
x = [10,20,30,40,50,60,70,80,90]
y = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function. Also provide the color and style for the point. Here we are going for green square point.
plt.plot(x,y, 'gs')

#Display the plot
plt.show()

###########################################

#7.2.4 Plotting a line
#import the pyplot module from matplotib library
import matplotlib.pyplot as plt

#define two lists for the values of x and y 
x = [10,20,30,40,50,60,70,80,90]
y = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function.
plt.plot(x,y)

#Display the plot
plt.show()
###############################################
#import the pyplot module from matplotib library
import matplotlib.pyplot as plt

#define two lists for the values of x and y 
x = [10,20,30,40,50,60,70,80,90]
y = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function. Magenta color,circle points on dotted line
plt.plot(x,y,"mo:")

#Display the plot
plt.show()

#######################################################3
#import the pyplot module from matplotib library
import matplotlib.pyplot as plt

#define two lists for the values of x and y 
x = [10,20,30,40,50,60,70,80,90]
y = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function. Magenta color,circle points on dotted line
plt.plot(x,y,"mo:", markersize = 9, linewidth = 3)

#Display the plot
plt.show()

######################################################3
#import the pyplot module from matplotib library
import matplotlib.pyplot as plt

#define two lists for the values of x and y 
x = [10,20,30,40,50,60,70,80,90]
y = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function. Magenta color,circle points on dotted line
plt.plot(x,y,"mo:", markersize = 9, linewidth = 3)

#Display the grid
plt.grid()

#Display plot
plt.show()

##########################################################
#7.2.5  Labelling the x and y axis
#import the pyplot module from matplotib library
import matplotlib.pyplot as plt

#define two lists for the values of x and y 
x = [10,20,30,40,50,60,70,80,90]
y = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function
plt.plot(x,y)

#Label the x-axis
plt.xlabel('X-axis')

#Label the y-axis
plt.ylabel('Y-axis')

#Give a title to the graph
plt.title('Simple Line Plot using PyPlot')

#Display the plot
plt.show()
###############################################################
#import the pyplot module from matplotib library
import matplotlib.pyplot as plt

#define two lists for the values of x1 and y1 
x1 = [10,20,30,40,50,60,70,80,90]
y1 = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function for values of x1 and y1
plt.plot(x1,y1)

#define two lists for the values of x2 and y2
x2 = [7,14,21,28,35,42,49,56,63]
y2 = [10,20,30,40,50,60,70,80,90]

#Call the plot(x,y) function for values of x2 and y2
plt.plot(x2,y2)

#Label the x-axis
plt.xlabel('X-axis')

#Label the y-axis
plt.ylabel('Y-axis')

#Give a title to the graph
plt.title('Plotting two lines on the same graph using PyPlot')

#Display the plot
plt.show()
########################################################################
#import the pyplot module from matplotib library
import matplotlib.pyplot as plt

#define two lists for the values of x1 and y1 
x1 = [10,20,30,40,50,60,70,80,90]
y1 = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function for values of x1 and y1 and assign it a label
plt.plot(x1,y1, label='Line for dataset x1, y1')

#define two lists for the values of x2 and y2
x2 = [7,14,21,28,35,42,49,56,63]
y2 = [10,20,30,40,50,60,70,80,90]

#Call the plot(x,y) function for values of x2 and y2 and assign it a label
plt.plot(x2,y2, label='Line for dataset x2, y2')

#Label the x-axis
plt.xlabel('X-axis')

#Label the y-axis
plt.ylabel('Y-axis')

#Give a title to the graph
plt.title('Plotting two lines on the same graph using PyPlot')

#invoke the legend function
plt.legend()

#Display the plot
plt.show()
