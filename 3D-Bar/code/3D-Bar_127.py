import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import io

# Add data to pandas dataframe
data="""Country,Life Expectancy (Years),Public Healthcare Expenditure (% GDP),Hospital Beds per 1000 People
 USA,78.6,17.2,2.77
 UK,81.1,9.8,2.54
 Germany,81.1,11.5,8.0
 Japan,84.5,10.9,13.05
 China,76.7,5.5,4.34"""
df = pd.read_csv(io.StringIO(data))
df.iloc[:, 1:] = df.iloc[:, 1:].astype(np.float32)

# Variables
x_values = df["Country"].tolist()
y_values = df.columns[1:].tolist()
data = df[y_values].values

# Initialize 3D plot
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# Create 3D bar plot for each column of data
width = depth = 0.2
space = 0.2
colors = ['r', 'g', 'b']
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), width, depth, 
              data[:,i], color=colors[i], alpha=0.8, zsort='average')

ax.set_title("Health and Healthcare Analysis by Country")
ax.set_xlabel('Country')
ax.set_ylabel('Metrics')
ax.set_zlabel('Value')

# Set x,y ticks  
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

# Create labels
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/97_202312302126.png')

# Clear image
plt.clf()
