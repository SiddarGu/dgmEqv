
import matplotlib.pyplot as plt
import numpy as np

#Data
Country = ['USA','UK','Germany','France']
Universities = [800,200,500,400]
Students = [30,10,20,15]

# Initializing the figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

#Plotting the bars
ax.bar(Country,Universities,label='Universities',color='red')
ax.bar(Country,Students,bottom=Universities,label='Students',color='blue')

# Labeling the bars
for i, v in enumerate(Universities):
    ax.text(i - 0.15, v + 0.5, str(v), color='red', fontsize=10, fontweight='bold')
for i, v in enumerate(Students):
    ax.text(i - 0.15, v + 0.5 +Universities[i], str(v), color='blue', fontsize=10, fontweight='bold', rotation=90, wrap=True)

#Plotting legend
plt.legend(loc='upper left')

#Setting the title
plt.title('Number of universities and students in four countries in 2021')

#Setting the ticks
plt.xticks(np.arange(len(Country)),Country)

#Setting the grid
plt.grid(axis='y', alpha=0.75)

#Adjust image size
plt.tight_layout()

#Save the image
plt.savefig("Bar Chart/png/519.png")

#Clear the current image state
plt.clf()