import matplotlib.pyplot as plt
import numpy as np

#Basic Graph
x = [0,1,2,3,4]
y = [2*i for i in x]

#Resize your Graph(dpi specifies pixels per inch. When saving probably should use 300 if possible)
plt.figure(figsize=(18,5), dpi=100)

#Line 1

#Keyword Argument Notation
plt.plot(x,y, label='2x', color='red', 
         linewidth=10, marker='.', 
         linestyle='--', 
         markersize=40, 
         markerfacecolor='yellow',
         markeredgecolor='blue')

# Add a legend (acts on the labels in the plt.plot)
plt.legend()

#Show plot
plt.show()



#------------------------------------------------------------
# Scatter Plot with custom colors and sizes
x = [1,2,3]
y = [4,5,6]
plt.scatter(x,y, color='red', marker="x")
plt.show()

#------------------------------------------------------------
# Scatter plot: Example 2
x = np.linspace(-5, 5, 150, endpoint=True)
y = np.sin(2*x)
plt.scatter(x, y, color='red',s=5, marker="o")
plt.show()

#------------------------------------------------------------
# Scatter plot: Example 3
t = np.arange(0.0, 5.0, 0.2)
# [fmt] = '[color][marker][line]'
plt.plot(t, t, 'r-*',
        t, t**2, 'bs', 
        t, t**3, 'g^')
plt.title('Multiple plots in one graph')
plt.legend(['t', 't**2', 't**3'])
plt.show()
#------------------------------------------------------------
# Randomized data and additional features
# Example 1
np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
plt.plot(x, y, "o")

# adding the regression line
# draw diagonal line from (70, 90) to (90, 200)
plt.plot([0, 100], [20,320],'r-')
plt.title("Randomized data")
plt.show()

#------------------------------------------------------------
# Other plot types

# generating a data set by a dictionary
mydata = {'a' : np.arange(50),
          'c' : np.random.randint(0, 50, 50),
          'd' : np.random.randn(50)}
# update the dictionary
mydata['b'] = mydata['a'] + 10 * np.random.randn(50)
mydata['d'] = np.abs(mydata['d']) * 100 

plt.scatter('a', 'b', 
            c='c', s='d', 
            data=mydata)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

#------------------------------------------------------------
# another example for scatter plot
x = [0, 2, 4, 6, 8, 10]
y = [0] * len(x)
mysize = [5 * 4**n for n in range(len(x))]
plt.scatter(x, y, s = mysize)
plt.show()

#------------------------------------------------------------
# another example for boxplot
x = [0, 2, 4, 6, 8, 10]
y = [0] * len(x)
mysize = [50 * 2**n for n in range(len(x))]
plt.scatter(x, y,
            s = mysize,
            color = 'red',
            marker = 5)
plt.show()

#------------------------------------------------------------
# subplot fig and ax Example
fig, ax = plt.subplots()
fig, ax = plt.subplots()
"""
`fig` is short for "figure" and represents the entire figure or the top-level container
that holds all the subplots, axes, images, and other elements of the plot.
`ax` is short for "axes" and represents a specific subplot or set of subplots
within the figure. An axes object is where you actually plot your data.
"""
# Add a point with a marker 'o' and size 10 to the first subplot
ax.plot([0], [0], marker = "o", markersize=10)
# Add a line with linewidth 10 from (0.07, 0) to (0.93, 0) to the first subplot
ax.plot([0.07, 0.93], [0, 0], linewidth=10)
# Add a scatter plot with a single point at (1, 0) and size 10**2 to the first subplot
ax.scatter([1], [0], s=10**2)
# Add a point with a marker '.' and size 22 to the second subplot
ax.plot([0], [1], marker=".", markersize=22)
# Add a line with linewidth 22 from (0.14, 1) to (0.86, 1) to the second subplot
ax.plot([0.14, 0.86], [1, 1], linewidth=22)
# Add a scatter plot with a single point at (1, 1) and size 22**2 to the second subplot
ax.scatter([1], [1], s=22**2)
# Show the plot
plt.show()
#------------------------------------------------------------
# Create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# Create a figure with two subplots arranged in one row and two columns
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
# Plot on the first subplot (ax[0])
ax[0].plot(x, y1, color='blue', label='Sin(x)')
ax[0].set_title('Sine Function')
ax[0].legend()
# Plot on the second subplot (ax[1])
ax[1].plot(x, y2, color='red', label='Cos(x)')
ax[1].set_title('Cosine Function')
ax[1].legend()
# Set common labels and title for the entire figure
fig.suptitle('Sine and Cosine Functions')
fig.tight_layout()
# Show the figure
plt.show()
#------------------------------------------------------------

x = [0,1,2,3,4]
y = [i^2 for i in x]
plt.plot(x,y,   label='2x', color='red',)