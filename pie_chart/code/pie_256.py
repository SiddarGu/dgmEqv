
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# Data
taxes = ['Income Tax','Property Tax','Excise Taxes','Sales Tax','Other Taxes']
percent = [30,15,25,20,10]

# Pie chart
ax.pie(percent, labels=taxes, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10},
       wedgeprops={'linewidth': 2, 'edgecolor': 'white'})

# Title
ax.set_title('Distribution of Taxation in the USA, 2023', fontsize=14, fontweight='bold')

# X-axis
plt.xticks(ticks=[], labels=[])

# Y-axis
plt.yticks(ticks=[], labels=[])

# Grids
ax.grid(True, zorder=1, which='major', axis='both', color='grey', alpha=0.15)

# Resize
plt.tight_layout()

# Save
plt.savefig('pie chart/png/520.png')

# Clear
plt.cla()