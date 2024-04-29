import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Parse the data string
data_string = 'Category,Number of Laws Enacted,Public Approval Rating,Government Spending (Millions of Dollars),Number of Civil Servants/n Education,200,60,5000,10000/n Healthcare,150,70,7000,8000/n Defense,100,50,10000,5000/n Transportation,120,65,4000,6000/n Environment,80,55,3000,4000/n Economy,180,75,9000,12000/n Social Welfare,90,45,6000,7000/n Justice,50,80,2000,3000/n Foreign Affairs,70,70,3000,2000/n Public Safety,110,65,5000,8000'
data_lines = data_string.split('/n')
data_headers = data_lines[0].split(',')
data_values = [line.split(',') for line in data_lines[1:]]

# create DataFrame from the parsed data
data_df = pd.DataFrame(data_values, columns=data_headers)

# transforming data into three variables
line_labels = data_df['Category']
data = data_df[data_df.columns[1:]].astype(int).values
data_labels = data_df.columns[1:]

# setup the figure and axes
fig = plt.figure(figsize=(15,8))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()

# positioning of the third and beyond y axis
ax3.spines['right'].set_position(('axes', 1.1))
ax4.spines['right'].set_position(('axes', 1.2))

# Plot the data
ax1.plot(line_labels, data[:,0], '-o', color='red', label=data_labels[0])
ax2.plot(line_labels, data[:,1], '-o', color='blue', label=data_labels[1])
ax3.bar(line_labels, data[:,2], color='green', label=data_labels[2], alpha=0.6)
ax4.scatter(line_labels, data[:,3], color='purple', label=data_labels[3])

# Formatting axes
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='red')
ax2.set_ylabel(data_labels[1], color='blue')
ax3.set_ylabel(data_labels[2], color='green')
ax4.set_ylabel(data_labels[3], color='purple')

# add grid, title
ax1.grid(True)
plt.title('Government and Public Policy Performance Analysis')

# add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower left')
ax4.legend(loc='lower right')

# automatically adjust the figure size
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/285_202312311430.png')

# clear current figure
plt.clf()
