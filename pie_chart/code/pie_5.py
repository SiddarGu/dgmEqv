
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Set figure size, title, legend positioning
plt.figure(figsize=(6,6))
plt.title('Sources of Donations to Charitable Organizations in the US, 2023')
plt.legend(loc='upper right')

# Set pie chart data and label, add percent in label
labels = ['Individuals', 'Foundations', 'Corporations', 'Government', 'Other']
sizes = [45, 20, 20, 10, 5]
texts = ['{}  {:.2f}%'.format(l,s) for l,s in zip(labels, sizes)]

# Set pie chart explode, color, autopct
explode = [0, 0, 0, 0, 0.1]
colors = ['#e6f2ff', '#b3e6ff', '#80ccff', '#4db8ff', '#1a9fff']
autopct = '%.2f%%'

# Plot pie chart
plt.pie(sizes, 
        explode=explode, 
        labels=texts, 
        colors=colors, 
        autopct=autopct, 
        shadow=True, 
        startangle=90)

# Set x ticks
plt.gca().xaxis.set_major_locator(mticker.NullLocator())

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/225.png', dpi=225)

# Clear the current image state
plt.clf()