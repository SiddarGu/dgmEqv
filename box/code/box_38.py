

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Restructure data
data = {'Employee Group': ['Entry Level', 'Experienced', 'Managerial', 'Senior', 'Executive'], 
        'Min Salary (USD)': [25000, 35000, 45000, 55000, 65000],
        'Q1 Salary (USD)': [30000, 45000, 60000, 70000, 80000],
        'Median Salary (USD)': [45000, 55000, 75000, 80000, 95000],
        'Q3 Salary (USD)': [60000, 70000, 90000, 95000, 110000],
        'Max Salary (USD)': [75000, 85000, 105000, 110000, 125000],
        'Outlier Salary (USD)': [[], [90000, 95000], [110000], [125000], []]
       }

# Create figure and plot data
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
data_values = [data['Min Salary (USD)'], data['Q1 Salary (USD)'], data['Median Salary (USD)'],
               data['Q3 Salary (USD)'], data['Max Salary (USD)']]
bp = ax.boxplot(np.array(data_values), patch_artist=True, labels=data['Employee Group'])

# Plot outliers manually
for i, outlier in enumerate(data['Outlier Salary (USD)']):
    if outlier:
        ax.plot([i + 1]*len(outlier), outlier, 'ro')

# Customize figure
ax.set_title('Salary Range Distribution of Different Employee Groups in 2020')
ax.set_ylabel('Salary Range (USD)')
ax.grid(linestyle='--')

# Auto adjust figure and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/7_202312251315.png')

# Clear the current image state
plt.clf()