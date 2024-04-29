
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei'] # set font
plt.rcParams['axes.unicode_minus'] = False # set font

# Create figure before plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Read data
data = [[2018, 100, 200, 300], [2019, 150, 250, 400], [2020, 90, 230, 320], [2021, 160, 270, 430], [2022, 110, 250, 360]]
df = pd.DataFrame(data, columns=['Year', 'Domestic Tourists', 'International Tourists', 'Total Tourists'])

# Plot the data 
ax.plot(df['Year'], df['Domestic Tourists'], 'b', marker='o', label='Domestic Tourists')
ax.plot(df['Year'], df['International Tourists'], 'r', marker='*', label='International Tourists')
ax.plot(df['Year'], df['Total Tourists'], 'g', marker='s', label='Total Tourists')

# Set x ticks to prevent interpolation
plt.xticks(df['Year'])

# Label the value of each data point directly on the figure
for xy in zip(df['Year'], df['Domestic Tourists']):
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
for xy in zip(df['Year'], df['International Tourists']):
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
for xy in zip(df['Year'], df['Total Tourists']):
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

# Set background grids
ax.grid(color='k', linestyle='-.', linewidth=1)

# Add legend
ax.legend(loc='upper left', fontsize=12)

# Set title
ax.set_title('Number of Tourists Visiting the United States from 2018 to 2022')

# Resize the image
plt.tight_layout()

# Save the image 
plt.savefig('line chart/png/414.png')

# Clear the current image state
plt.close()