
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(12, 8))

# Plot Data
plt.plot(
    [1990, 1995, 2000, 2005],
    [5, 9, 12, 18],
    label='Inventions A',
    linewidth=3,
    color='#07f0e9'
)
plt.plot(
    [1990, 1995, 2000, 2005],
    [7, 8, 6, 4],
    label='Inventions B',
    linewidth=3,
    color='#e907f9'
)
plt.plot(
    [1990, 1995, 2000, 2005],
    [3, 5, 8, 13],
    label='Inventions C',
    linewidth=3,
    color='#f9e907'
)
plt.plot(
    [1990, 1995, 2000, 2005],
    [10, 11, 14, 17],
    label='Inventions D',
    linewidth=3,
    color='#07a9f9'
)

# Set labels
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Inventions', fontsize=12)

# Set xticks
plt.xticks([1990, 1995, 2000, 2005], fontsize=12)

# Set title
plt.title('Number of Inventions across Four Fields in the Last 30 Years', fontsize=14)

# Add legend
plt.legend(loc='upper left')

# Resize the figure
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/135.png')

# Clear the figure
plt.clf()