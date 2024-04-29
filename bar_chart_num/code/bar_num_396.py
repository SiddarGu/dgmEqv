
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(15,6))

# Get data
months = ['January', 'February', 'March', 'April']
Wind_Energy = [20, 25, 30, 35]
Solar_Energy = [30, 35, 40, 45]
Hydro_Energy = [40, 45, 50, 55]

# Create bar chart
ax = fig.add_subplot(111)
ax.bar(months, Wind_Energy, width=0.2, color='b', label='Wind Energy')
ax.bar(months, Solar_Energy, width=0.2, bottom=Wind_Energy, color='g', label='Solar Energy')
ax.bar(months, Hydro_Energy, width=0.2, bottom=[w+s for w,s in zip(Wind_Energy, Solar_Energy)], color='r', label='Hydro Energy')

# Label value of each data point for every variables directly on the figure
for i, v in enumerate(Wind_Energy):
    ax.text(i-.08, v+3, str(v))
for i, v in enumerate(Solar_Energy):
    ax.text(i-.08, v+3+Wind_Energy[i], str(v))
for i, v in enumerate(Hydro_Energy):
    ax.text(i-.08, v+3+Wind_Energy[i]+Solar_Energy[i], str(v))

# Get legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3)

# Set title
ax.set_title('Energy production from renewable sources from January to April 2021')

# Set xticks
ax.set_xticks(months)

# Automatically resize the image 
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/122.png', bbox_inches='tight')

# Clear current image 
plt.clf()