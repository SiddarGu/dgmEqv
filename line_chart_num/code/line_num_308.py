
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Plot line chart
ax.plot(['18-24','25-34','35-44','45-54'], [45000, 55000, 70000, 90000], color = 'darkorange', marker = 'o', linestyle = '-', linewidth = 2, label = 'Average Income')
ax.plot(['18-24','25-34','35-44','45-54'], [25, 40, 25, 10], color = 'dodgerblue', marker = 'o', linestyle = '-', linewidth = 2, label = 'Percent of Population')

# Set the title
ax.set_title('Average Income and Population Distribution by Age Group in the USA, 2023', fontname='Arial', fontsize=20)

# Set the x-axis label
ax.set_xlabel('Age Group', fontsize=15, fontname='Arial')

# Set the y-axis label
ax.set_ylabel('Average Income (dollars) / Percent of Population', fontsize=15, fontname='Arial')

# Set the x-axis ticks and labels
ax.xaxis.set_major_locator(ticker.MaxNLocator(4))
ax.set_xticklabels(['18-24','25-34','35-44','45-54'], fontname='Arial', fontsize=14)

# Set the y-axis ticks and labels
ax.yaxis.set_major_locator(ticker.MaxNLocator(5))
ax.set_yticklabels([0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000], fontname='Arial', fontsize=14)

# Display legend
ax.legend(loc='upper left', fontsize=14)

# Annotate value of each data point directly on the figure
for i,j in zip(['18-24','25-34','35-44','45-54'], [45000, 55000, 70000, 90000]):
    ax.annotate(str(j), xy=(i,j), fontsize=14, fontname='Arial')

for i,j in zip(['18-24','25-34','35-44','45-54'], [25, 40, 25, 10]):
    ax.annotate(str(j), xy=(i,j), fontsize=14, fontname='Arial')

# Add a background grid
ax.grid(linestyle='--', linewidth=0.5)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/224.png')

# Clear the current image state
plt.clf()