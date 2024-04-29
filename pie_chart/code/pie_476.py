
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

# Data to plot
labels = ['Music', 'Painting', 'Sculpture', 'Photography', 'Theater', 'Film & TV', 'Dance', 'Literature']
sizes = [20, 15, 15, 15, 10, 15, 10, 10]

# Plot pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Set a title
ax.set_title('Popularity of Art Forms in the USA, 2023')

# Show legend
ax.legend(loc="best", bbox_to_anchor=(1, 0.5))

# Make sure all characters show
plt.xticks(rotation=-45, ha="left")

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/79.png')

# Clear current image state
plt.clf()