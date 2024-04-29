

import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(9,5))

# Create subplots
ax = plt.subplot()

# Set labels
ax.set_title('Average hourly production rate change in a manufacturing plant')
ax.set_ylabel('Production rate (units/hour)')
ax.set_xlabel('Month')

# Get data
months = ['January','February','March','April','May']
production_rate_A = [100,90,125,110,95]
production_rate_B = [120,110,115,105,95]
production_rate_C = [130,140,145,135,125]

# Set xticks
locs = np.arange(len(months))
plt.xticks(locs,months)

# Plot data
ax.plot(production_rate_A, marker='o', label='Production rate A', linestyle='dashed')
ax.plot(production_rate_B, marker='^', label='Production rate B')
ax.plot(production_rate_C, marker='s', label='Production rate C', linestyle='dotted')

# Annotate data points
for x,y in zip(locs,production_rate_A):
    ax.annotate('{}'.format(y), xy=(x,y), xytext=(x, y+5))
for x,y in zip(locs,production_rate_B):
    ax.annotate('{}'.format(y), xy=(x,y), xytext=(x, y+5))
for x,y in zip(locs,production_rate_C):
    ax.annotate('{}'.format(y), xy=(x,y), xytext=(x, y+5))

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1, 0.9), prop={'size':8})
    
# Resize figure
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/574.png')

# Clear figure
plt.clf()