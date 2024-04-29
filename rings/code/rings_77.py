
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Efficiency', 'Quality Control', 'Cost Control', 'Logistics', 'Automation']
data = np.array([39, 13, 27, 7, 14])
line_labels = ['Category', 'ratio']

# Plot the data with the type of rings chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
ax.pie(data, startangle=90, counterclock=False, colors=['g', 'y', 'b', 'c', 'm'])
centre_circle = plt.Circle((0, 0), 0.6, color='black', fc='white', linewidth=0)
ax.add_artist(centre_circle)
ax.legend(data_labels, loc='best')
ax.set_title('Manufacturing and Production Efficiency - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_146.png')

plt.close('all')