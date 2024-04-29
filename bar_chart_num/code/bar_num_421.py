
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Define data
countries = ['USA', 'UK', 'Germany', 'France']
museums = [20, 25, 15, 30]
galleries = [50, 60, 40, 55]
theaters = [30, 45, 25, 35]

# Create x-axis
x = range(len(countries))

# Plot data
ax.bar(x, museums, bottom=theaters, color='skyblue', label='Museums')
ax.bar(x, theaters, color='orange', label='Theaters')
ax.bar(x, galleries, bottom=museums, color='darkseagreen', label='Galleries')

# Set tick labels
ax.set_xticks(x)
ax.set_xticklabels(countries)

# Set title
ax.set_title("Number of Arts and Culture centers in four countries in 2021")

# Set legend
ax.legend(loc='upper right')

# Annotate bars
for bar, museum, gallery, theater in zip(x, museums, galleries, theaters):
    # Add text
    ax.text(bar, museum/2 + theater, str(museum), ha='center', va='bottom', color='w', fontsize=11)
    ax.text(bar, museum + gallery/2, str(gallery), ha='center', va='bottom', color='w', fontsize=11)
    ax.text(bar, museum + theater + gallery/2, str(theater), ha='center', va='bottom', color='w', fontsize=11)

# Resize the image to fit the content
plt.tight_layout()

# Save the image
plt.savefig('Bar Chart/png/543.png')

# Clear the current image state
plt.clf()