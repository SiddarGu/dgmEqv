
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot()

# Set data
x = np.arange(2000, 2005)
y1 = [1000, 1200, 1500, 1300, 1800]
y2 = [20, 25, 30, 35, 40]
y3 = [200, 220, 250, 280, 300]

# Draw line chart
ax.plot(x, y1, label = 'Number of Cases', linewidth = 2)
ax.plot(x, y2, label = 'Number of Judges', linewidth = 2)
ax.plot(x, y3, label = 'Number of Lawyers', linewidth = 2)

# Set labels
ax.set_title('Increase in legal cases and legal profession in the United States from 2000 to 2004')
ax.set_xlabel('Year')
ax.set_ylabel('Number')

# Set xticks
xticks_labels = [str(i) for i in x]
ax.set_xticks(x)
ax.set_xticklabels(xticks_labels)

# Set grids
ax.grid(axis='y', linestyle='-.', alpha=0.4, linewidth=1)

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# Annotate data points
for a,b in zip(x,y1):
    ax.annotate(str(b),xy=(a,b))
for c,d in zip(x,y2):
    ax.annotate(str(d),xy=(c,d))
for e,f in zip(x,y3):
    ax.annotate(str(f),xy=(e,f))

# Resize the figure
fig.tight_layout()

# Save the figure
plt.savefig('line chart/png/145.png')

# Clear current image
plt.clf()