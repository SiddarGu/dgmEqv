
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Create a figure
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(1,1,1)

# Set plot data
x = [2017, 2018, 2019, 2020]
y1 = [1000, 1200, 800, 1500]
y2 = [800, 900, 1100, 1200]
y3 = [1200, 1100, 1300, 1400]
y4 = [1500, 1600, 1200, 800]

# Plot the line
ax.plot(x, y1, label='Donations A (million dollars)', color='#539caf', linewidth=1, marker='o', markersize=4, markerfacecolor='#539caf', markeredgecolor='#539caf')
ax.plot(x, y2, label='Donations B (million dollars)', color='#7663b0', linewidth=1, marker='o', markersize=4, markerfacecolor='#7663b0', markeredgecolor='#7663b0')
ax.plot(x, y3, label='Donations C (million dollars)', color='#1f77b4', linewidth=1, marker='o', markersize=4, markerfacecolor='#1f77b4', markeredgecolor='#1f77b4')
ax.plot(x, y4, label='Donations D (million dollars)', color='#ff7f0e', linewidth=1, marker='o', markersize=4, markerfacecolor='#ff7f0e', markeredgecolor='#ff7f0e')

# Set x ticks
x_ticks = [2017, 2018, 2019, 2020]
ax.set_xticks(x_ticks)

# Set title
ax.set_title('Donations to four charities in the past four years')

# Set x-axis label
ax.set_xlabel('Year')

# Set y-axis label
ax.set_ylabel('Donations (million dollars)')

# Add grid
ax.grid(linestyle='-', linewidth='0.5', color='gray')

# Add legend
ax.legend(loc='upper right', frameon=False)

# Add annotation
ax.annotate('A', xy=(2017, 1000), xytext=(2018, 1300), fontsize=12, arrowprops=dict(facecolor='#539caf', arrowstyle='->'))
ax.annotate('B', xy=(2018, 900), xytext=(2017, 1100), fontsize=12, arrowprops=dict(facecolor='#7663b0', arrowstyle='->'))
ax.annotate('C', xy=(2019, 1300), xytext=(2018, 1500), fontsize=12, arrowprops=dict(facecolor='#1f77b4', arrowstyle='->'))
ax.annotate('D', xy=(2020, 800), xytext=(2019, 1000), fontsize=12, arrowprops=dict(facecolor='#ff7f0e', arrowstyle='->'))

# Resize the figure
plt.tight_layout()

#Save the figure
plt.savefig('line chart/png/38.png')

# Clear the current figure
plt.clf()