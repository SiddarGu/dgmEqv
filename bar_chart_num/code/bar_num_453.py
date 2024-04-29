
import matplotlib.pyplot as plt
import numpy as np

#Create figure 
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

#Data
Country = ['USA', 'UK', 'Germany', 'France']
Museums = [20, 25, 15, 18]
Theatres = [15, 10, 20, 18]
Galleries = [25, 30, 20, 28]

#Position of the x-axis labels
x_pos = np.arange(len(Country))

#Set width of each bar
width = 0.25

#Plotting the bars
ax.bar(x_pos, Museums, width, label='Museums')
ax.bar(x_pos + width, Theatres, width, label='Theatres')
ax.bar(x_pos + width*2, Galleries, width, label='Galleries')

#Set the y-axis label
ax.set_ylabel('Number of Facilities')

#Set the chart's title
ax.set_title('Number of Arts and Culture Facilities in four countries in 2021')

#Set the position of the x ticks
ax.set_xticks(x_pos + width / 2)

#Set the labels for the x ticks
ax.set_xticklabels(Country)

#Adding the legend and showing the plot
ax.legend(loc = 'upper left')

#Adding the value of each data point for every variables directly on the figure
for i, v in enumerate(Museums):
    ax.text(i - 0.15, v + 1, str(v))
for i, v in enumerate(Theatres):
    ax.text(i + 0.1, v + 1, str(v))
for i, v in enumerate(Galleries):
    ax.text(i + 0.35, v + 1, str(v))

#Adjust the size of the figure
plt.tight_layout()

#Save the figure
plt.savefig('Bar Chart/png/149.png')

#Clear the current image state
plt.clf()