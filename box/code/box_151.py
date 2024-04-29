import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Charity A', 'Charity B', 'Nonprofit C', 'Charity D', 'Nonprofit E']

data_2d = [[100, 200, 300, 400, 500],
           [150, 250, 350, 450, 550], 
           [120, 220, 320, 420, 520],
           [130, 230, 330, 430, 530],
           [110, 210, 310, 410, 510]]

outliers = [[], [50,800], [900], [], [20,600]]

# Create figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111) 

# Box plot
bp = ax.boxplot(data_2d, notch=True, patch_artist=True, boxprops=dict(facecolor="C0"), whis=1.5)

ax.set_yticks(np.arange(0,1001,100))
ax.set_xticklabels(categories, rotation=45)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)

# Outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i+1]*len(outlier), outlier, "X", color='red') 

# Labels and Titles
ax.set_title('Donation Distribution in Charities and Nonprofit Organizations (2022)')
ax.set_xlabel('Organization')
ax.set_ylabel('Donation ($)')

# Save figure
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/168_202312310058.png', bbox_inches='tight')

# Clear figure
plt.close(fig)
