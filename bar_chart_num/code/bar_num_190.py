
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,8))

# Define data
countries = ['USA', 'UK', 'Germany', 'France']
solar = [30, 20, 25, 35]
wind = [50, 60, 55, 45]
hydro = [20, 25, 30, 35]

# Plot bar chart
xpos = np.arange(len(countries))

ax = fig.add_subplot()
ax.bar(xpos-0.2, solar, width=0.2, align='center', label='Solar')
ax.bar(xpos, wind, width=0.2, align='center', label='Wind')
ax.bar(xpos+0.2, hydro, width=0.2, align='center', label='Hydro')

# Annotate value of each data point
for x,y in zip(xpos, solar):
    ax.annotate(y, (x-0.2,y+2))
for x,y in zip(xpos, wind):
    ax.annotate(y, (x,y+2))
for x,y in zip(xpos, hydro):
    ax.annotate(y, (x+0.2,y+2))

# Set xticks
ax.set_xticks(xpos)
ax.set_xticklabels(countries)

# Set title
ax.set_title('Energy production from solar, wind and hydro sources in four countries in 2021')

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/505.png')

# Clear the current image state
plt.clf()