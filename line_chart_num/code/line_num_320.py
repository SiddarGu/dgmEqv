
import matplotlib.pyplot as plt
import numpy as np

# Create figure and add subplot
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(1,1,1)

# Set the y-axis label
ax.set_ylabel('Rate (%)', fontsize=16)

# Set the x-axis label
ax.set_xlabel('Year', fontsize=16)

# Set the title
ax.set_title("Economic Performance in the United States from 2001 to 2004", fontsize=20)

# Set the font color
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')

# Set the xticks
x_data = ['2001','2002','2003','2004']
plt.xticks(np.arange(4), x_data, fontsize=14)

# Set the yticks
y_data = np.arange(0,7.5,0.5)
plt.yticks(y_data, fontsize=14)

# Set the legend
Unemp_Rate = plt.plot(np.arange(4), [4,3,2,5], color='b', label='Unemployment Rate') 
Inflation_Rate = plt.plot(np.arange(4), [2,4,3,6], color='orange', label='Inflation Rate') 
GDP_Growth_Rate = plt.plot(np.arange(4), [4,3,2,1], color='g', label='GDP Growth Rate')
Gini_Coefficient = plt.plot(np.arange(4), [50,51,52,53], color='r', label='Gini Coefficient')
ax.legend(loc='upper right', fontsize=14)

# Set the grid
plt.grid(True, linewidth=1, color='#AAAAAA', linestyle='--')

# Annotate the value of each data point directly on the figure
for a, b in zip(np.arange(4), [4,3,2,5]):
    ax.annotate(str(b), xy=(a,b), fontsize=12)
for a, b in zip(np.arange(4), [2,4,3,6]):
    ax.annotate(str(b), xy=(a,b), fontsize=12)
for a, b in zip(np.arange(4), [4,3,2,1]):
    ax.annotate(str(b), xy=(a,b), fontsize=12)
for a, b in zip(np.arange(4), [50,51,52,53]):
    ax.annotate(str(b), xy=(a,b), fontsize=12)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/23.png')

# Clear the current image state
plt.clf()