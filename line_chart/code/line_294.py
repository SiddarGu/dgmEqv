
import matplotlib.pyplot as plt
import numpy as np

#set the size of the chart
plt.figure(figsize=(10,6))

#Adding the subplot
ax=plt.subplot()

#Add data
year=[2010,2011,2012,2013]
wheat=[10000,12000,9000,11000]
rice=[15000,14000,13000,15000]
maize=[8000,8000,8000,8000]
barley=[6000,7000,6000,8000]

#Setting the labels of x and y axis
ax.set_xlabel("Year")
ax.set_ylabel("Tons")

#Setting the title of the chart
plt.title("Crop Production in the USA from 2010 to 2013")

#Plotting the data
ax.plot(year,wheat,label="Wheat")
ax.plot(year,rice,label="Rice")
ax.plot(year,maize,label="Maize")
ax.plot(year,barley,label="Barley")

#Adding the legend
plt.legend(loc="upper left", bbox_to_anchor=(1,1))

#Setting the xticks
plt.xticks(np.arange(min(year), max(year)+1, 1.0))

#Adding the grid
ax.grid(linestyle="--", linewidth="0.5", color="black")

#Displaying the chart
plt.tight_layout()
plt.show()

#Saving the image
plt.savefig("line chart/png/120.png")

#Clear the current image state
plt.clf()