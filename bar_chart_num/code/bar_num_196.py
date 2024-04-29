
import matplotlib.pyplot as plt
import numpy as np

# Generate data
Country = ['USA','UK','Germany','France']
Museums = [10,12,13,8]
Galleries = [15,14,17,11]
Theatres = [20,18,21,16]

# Generate Figure
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111)

# Plot data
bar_width = 0.2
ax.bar(np.arange(len(Country)), Museums, width=bar_width, label='Museums', color='#FF9999')
ax.bar(np.arange(len(Country))+bar_width, Galleries, width=bar_width, label='Galleries', color='#99CCFF')
ax.bar(np.arange(len(Country))+2*bar_width, Theatres, width=bar_width, label='Theatres', color='#FFFF99')

#Label x-axis
ax.set_xticks(np.arange(len(Country)) + bar_width)
ax.set_xticklabels(Country)

# Add title and legend
plt.title('Number of cultural venues in four countries in 2021')
plt.legend(loc="upper right")

# Label value of each data point
for i in range(len(Country)):
    ax.annotate(Museums[i], xy=(i-0.2, Museums[i]+0.8), xytext=(0, 0), textcoords="offset points", ha='center', va='bottom')
    ax.annotate(Galleries[i], xy=(i, Galleries[i]+0.8), xytext=(0, 0), textcoords="offset points", ha='center', va='bottom')
    ax.annotate(Theatres[i], xy=(i+0.2, Theatres[i]+0.8), xytext=(0, 0), textcoords="offset points", ha='center', va='bottom')

# Resize the figure
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/47.png')

# Clear the current image state
plt.cla()