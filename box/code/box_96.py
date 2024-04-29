import matplotlib.pyplot as plt
import numpy as np

# Original data
data = """Energy Source,Min Cost ($),Q1 Cost ($),Median Cost ($),Q3 Cost ($),Max Cost ($),Outlier Cost ($)
Coal,1000,3000,5000,7000,10000,[]
Natural Gas,1500,3500,5500,7500,10500,[500]
Hydro,800,2700,4500,6300,9000,[1200,11000]
Solar,1000,2900,4700,6500,9200,[400,1300]
Wind,750,2750,4750,6750,9500,[]"""

# Data is restructured
lines = data.split("\n")[1:]
labels = [line.split(",")[0] for line in lines]
values = [list(map(int, line.split(",")[1:6])) for line in lines]
outliers = [[int(val) for val in list.replace("[", "").replace("]", "").split(",") if val != ''] for list in [line.split(",")[6] for line in lines]]

# Create figure
fig = plt.figure(figsize = (10,8))
ax = fig.add_subplot(111)

# Plot boxplot and outliers
ax.boxplot(values, whis = 1.5)
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Set properties
ax.set_xticklabels(labels, rotation = 45,  ha = "right")
ax.set_ylabel('Cost ($)')
ax.set_title('Operational Cost Distribution in Different Energy Sources (2022)')
plt.grid()

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/102_202312270030.png')

# Clear the current image 
plt.clf()
