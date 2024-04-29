
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 8))

# Get data
labels = ['Road', 'Rail', 'Air', 'Water']
sizes = [50, 25, 20, 5] 

# Plot
plt.pie(sizes, labels=labels, colors=['red', 'green', 'blue', 'yellow'], 
    autopct='%.2f%%', shadow=True, startangle=90, rotatelabels=True,
    wedgeprops={'linewidth':2,'edgecolor':"black"})

# Set title
plt.title("Distribution of Transportation Modes in the US, 2023")

fig.tight_layout()
plt.xticks(np.arange(0,360,90))
plt.savefig('pie chart/png/367.png')

# Clear figure
plt.clf()