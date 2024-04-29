
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels

data_labels = ['Electricity', 'Natural Gas', 'Nuclear', 'Renewable', 'Oil', 'Coal', 'Water', 'Telecommunications']
data = [90, 80, 70, 60, 50, 40, 30, 20]
line_labels = ['Category','Number']

# Plot the data with the type of rose chart

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='polar') 

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories 

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=plt.cm.Set1(i), label=data_labels[i])

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14, ha='center', wrap=True)

fig.suptitle('Utilization of Energy and Utility Resources in the US in 2021', fontsize=20)

plt.grid(color='gray', linestyle='--', linewidth=1)

plt.tight_layout()

# save the image

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_142.png')

# Clear the current image state

plt.clf()