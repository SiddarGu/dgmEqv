import matplotlib.pyplot as plt
import numpy as np

# Parse your given data
given_data = "Disease Type,Age Group 20-30,Age Group 30-40,Age Group 40-50,Age Group 50-60/n Diabetes,70,75,80,85/n Heart Disease,40,45,50,55/n Cancer,60,65,70,75/n Liver Disease,55,60,65,70/n Respiratory Diseases,45,50,55,60"
rows = given_data.split('/n')
data_labels = [col.strip() for col in rows[0].split(',')]
data_labels = data_labels[1:]
line_labels = []
data = []
for row in rows[1:]:
    values = row.split(',')
    line_labels.append(values[0].strip()) 
    data.append([int(v) for v in values[1:]])

# Plotting 
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

max_value = max([max(row) for row in data])
for idx, row in enumerate(data):
    row.append(row[0]) 
    ax.plot(angles, row, label=line_labels[idx])
    ax.fill(angles, row, alpha=0.1)
    radius = np.full_like(angles, ((idx+1) * max_value / len(data)))
    ax.plot(angles, radius, color='grey', ls='--')

ax.set_rlim(0, max_value * 1.1)  
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.spines['polar'].set_visible(False)
ax.set(title='Health Condition Prevalence By Age Group')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/138_2023122292141.png')
plt.clf()
