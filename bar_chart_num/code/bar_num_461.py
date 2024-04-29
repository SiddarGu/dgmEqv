
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig=plt.figure(figsize=(10,6))

# Data
Country = ['USA', 'UK', 'Germany', 'France']
Museums = [20, 30, 18, 23]
Theaters = [40, 50, 36, 46]
Galleries = [80, 90, 72, 92]

# Stacking bars
x = np.arange(len(Country))
width = 0.2
ax = fig.add_subplot(111)
ax.bar(x-width, Museums, width, label='Museums')
ax.bar(x, Theaters, width, label='Theaters')
ax.bar(x+width, Galleries, width, label='Galleries')

# Setting ticks
ax.set_xticks(x)
ax.set_xticklabels(Country)

# Labeling values
bottom_list = [sum(x) for x in zip(Museums, Theaters)]

for i in range(len(Country)):
    ax.annotate(Galleries[i], xy=(x[i]+width/2, Galleries[i]+2), xytext=(x[i]+width/2, Galleries[i]+2), fontsize=10, va='bottom', ha='center')
    ax.annotate(Theaters[i], xy=(x[i], Theaters[i]+2), xytext=(x[i], Theaters[i]+2), fontsize=10, va='bottom', ha='center')
    ax.annotate(Museums[i], xy=(x[i]-width/2, Museums[i]+2), xytext=(x[i]-width/2, Museums[i]+2), fontsize=10, va='bottom', ha='center')

# Adding legend
ax.legend(bbox_to_anchor=(1, 1))

# Adding title
ax.set_title('Cultural institutions in four countries in 2021')

# Tight layout
fig.tight_layout()

# Saving figure
fig.savefig('Bar Chart/png/365.png')

# Clear the current image state
plt.clf()