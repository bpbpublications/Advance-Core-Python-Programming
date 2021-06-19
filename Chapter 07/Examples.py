#import numpy
import numpy as np

#import PyPlot
import matplotlib.pyplot as plt

#define array have values from 20 to 40, 5 values apart
x = np.arange(20,40,5)

# define f(x) = log(x)
y = np.log(x)

#Call the plot() function
plt.plot(x,y)

#Label the x-axis
plt.xlabel("x values from 20-40, 5 steps apart")

#label the y - axis
plt.ylabel("f(x) = log(x)")

#Give a title to the plot
plt.title("f(x) vs. x")

#Display the plot
plt.show()
######################################################################3
#Example 7.5
#import PyPlot
import matplotlib.pyplot as plt

#import NumPy
import numpy as np

#Define start, end and step values of the range
start = int(input("Enter the starting point of the range : "))
end = int(input("Enter the end point of the range : "))
step = int(input("Enter the interval between two consecutive values : "))

#define array for x-axis
x = np.arange(start,end,step)

# define array for y-axis
y = (x**2)+(3*x)

#Call the plot() function
plt.plot(x,y)


#Label the x-axis
plt.xlabel("X-axis")

#label the y - axis
plt.ylabel("Y-axis")

#Give a title to the plot
plt.title("plotting of function")

# Display the plot
plt.show()
#########################################################################3
#Example 7.6
#import PyPlot
import matplotlib.pyplot as plt

#define array of country names
x = ['China','India','USA','Indonesia','Brazil','Nigeria','Bangladesh']

# define array of population
y = [1384688986,1296834042,329256465,262787403,208846892,195300343,159453001]

#Call the bar() function
plt.bar(x,y)

#Label the x-axis
plt.xlabel("Country")

#label the y - axis
plt.ylabel("Population")

#Give a title to the plot
plt.title("Country vs. Population")

# Display the plot
plt.show()
#################################################################3
#Example 7.7
#import PyPlot
import matplotlib.pyplot as plt

#define arrays of Science Student id and Score
x1 = [101,104,108,109,110,112]
y1 = [78,57,89,99,86,72]

# define arrays of commerce Students id and Score
x2 = [102,103,105,106,107,111]
y2 = [89,100,98,67,100,20]

#Call the plot() function
plt.bar(x1,y1,label='Science department')
plt.bar(x2,y2,label='Commerce department')

#Label the x-axis
plt.xlabel("Student id")

#label the y - axis
plt.ylabel("%Score")

#Give a title to the plot
plt.title("Score for Science and Commerce Students")

plt.legend()

# Display the plot
plt.show()
###############################################################
#Example 7.8
#import PyPlot
import matplotlib.pyplot as plt

#import NumPy
import numpy as np

#define array of Student Name
x = ['John','Ted','Lizy','Elena','Alex','Albert','Meg']

# define array of Student Score
arr = np.array([376,455,489,300,250,340,400])
y = arr*100/500

#Call the plot() function
plt.bar(x,y)

#Label the x-axis
plt.xlabel("Student name")

#label the y - axis
plt.ylabel("%Score")

#Give a title to the plot
plt.title("Score")

# Display the plot
plt.show()

###################################################3
#Example 7.9
import matplotlib.pyplot as plt
# Data to plot
gases = ['Nitrogen', 'O2', 'Co2', 'others']
sizes = [78,20,0.3,1.97]
colors = ['pink', 'yellow','orange', 'lightskyblue']

# Plot
plt.pie( sizes,explode=(0, 0.1, 0, 0),labels =gases,colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.legend()
plt.show()
