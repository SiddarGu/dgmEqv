
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Renewable Energy', 'Natural Gas', 'Nuclear Energy', 'Oil']
data = [25, 40, 20, 15]
line_labels = ['Category', 'Ratio']

# Plot the data with the type of rings chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%')
inner_circle = plt.Circle((0,0),0.7,color='white')
ax.add_artist(inner_circle)

# For the plot of legend
ax.legend(data_labels, loc='upper right')

# Drawing techniques such as background grids can be used
ax.grid(True)

# The title of the figure should be  Energy and Utilities Consumption Overview - 2023
ax.set_title("Energy and Utilities Consumption Overview - 2023")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_12.png
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_12.png')

# Clear the current image state at the end of the code
plt.clf()