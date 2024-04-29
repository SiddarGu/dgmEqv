
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Data
data = np.array([[50,100,200], [40,90,180], [30,80,170], [35,85,185]])

# Define countries
countries = ['USA', 'UK', 'Germany', 'France']

# Define categories
categories = ['Grains', 'Vegetables', 'Fruits']

# Define colors
colors = ['#54d8ff', '#f7ae3d', '#f75a3d']

# Plot
plt.title('Food Production of Grains, Vegetables, and Fruits in four countries in 2021')
ax.set_xticks([0,1,2,3])
ax.set_xticklabels(countries)
ax.set_ylabel('Production (tons)')

# Plot data
start = 0
for i, category in enumerate(categories):
    ax.bar(np.arange(len(countries)), data[:,i], bottom=start, label=category, color=colors[i])
    start += data[:,i]

# Annotate
for x,y,category in zip(np.arange(len(countries)), data[:,2], categories):
    ax.annotate(y, (x,y/2), ha='center', va='center', rotation='vertical', wrap=True)

# Legend
plt.legend(loc='upper left')

# Adjustment
plt.tight_layout()

# Save
plt.savefig('Bar Chart/png/198.png')

# Clear
plt.clf()