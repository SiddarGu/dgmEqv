
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Crop Yields','Irrigation','Soil Quality','Pesticide Use','Productivity']
data = [30,15,35,10,10]
line_labels = ['Category','ratio']

# Plot the data with the type of rings chart
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%', colors=['#ffb732','#cef442','#2cef45','#2cef8d','#2c9efb'])

# To change the pie chart into a ring chart in your code
inner_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(inner_circle)

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout.
ax.legend(data_labels,loc='lower left', bbox_to_anchor=(-0.1, -0.1))

# Drawing techniques such as background grids can be used.
ax.grid(linestyle='--', linewidth=0.5, color='black', alpha=0.3)

# The title of the figure should be  Agricultural Output and Food Production - 2023.
plt.title('Agricultural Output and Food Production - 2023', fontsize=15)
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_95.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_95.png')

# Clear the current image state at the end of the code.
plt.clf()