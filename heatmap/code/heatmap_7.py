
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Import seaborn as sns if using sns.heatmap()
import seaborn as sns

#Create a dictionary to store the data
data = {"Country": ["United States", "China", "India", "Japan", "Germany", "United Kingdom"],
        "Primary Education Completion Rate (%)": [92, 98, 97, 100, 95, 90],
        "Secondary Education Completion Rate (%)": [88, 95, 92, 98, 90, 85],
        "Tertiary Education Completion Rate (%)": [65, 80, 70, 95, 80, 75],
        "Literacy Rate (%)": [99, 99, 85, 99, 98, 97],
        "Enrollment Rate (%)": [95, 98, 90, 100, 96, 92]}

#Convert the dictionary to a pandas dataframe
df = pd.DataFrame(data)

#Set the index to be the Country column
df = df.set_index("Country")

#Create a figure and axes
fig, ax = plt.subplots(figsize=(10,8))

#Plot the heatmap using sns.heatmap() or imshow() or pcolor()
heatmap = sns.heatmap(df, annot=True, linewidths=.5, ax=ax) #Use annot=True to show the values in each cell
#heatmap = ax.imshow(df, cmap="coolwarm", vmin=0, vmax=100) #Use cmap="coolwarm" to set the color scheme and vmin/vmax to set the range of values

#Set the title
ax.set_title("Education Metrics by Country", fontsize=18)

#Set the x and y labels
ax.set_xlabel("Education Completion Rate (%)", fontsize=12)
ax.set_ylabel("Country", fontsize=12)

#Set the x and y tick labels in the center of each row and column
ax.set_xticks(np.arange(len(df.columns))+0.5)
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(np.arange(len(df.index))+0.5)
ax.set_yticklabels(df.index, rotation=0, ha="right", rotation_mode="anchor")

#Automatically resize the image and add a colorbar if desired
fig.tight_layout() #Use tight_layout() to automatically resize the image
#fig.colorbar(heatmap) #Use this line if you want to add a colorbar to the plot

#Save the figure as a png file
plt.savefig("output/final/heatmap/png/20231225-210514_23.png", bbox_inches="tight") #Use bbox_inches="tight" to prevent the labels from being cut off

#Clear the current image state
plt.clf()