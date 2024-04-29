
# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create dictionary with data
data = {'Area of Study': ['Undergraduate', 'Masters', 'PhD', 'Certificate Programs', 'Vocational Programs'],
        'Mathematics (Students)': [500, 300, 200, 150, 100],
        'Computer Science (Students)': [800, 600, 400, 300, 200],
        'Biology (Students)': [700, 500, 300, 200, 150],
        'Chemistry (Students)': [600, 400, 200, 250, 100],
        'Physics (Students)': [700, 500, 300, 200, 150]}

# convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# plot the data with area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.columns[1:])

# set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# calculate max total value and set y axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 10:
    max_total_value = np.ceil(max_total_value)
elif max_total_value <= 100:
    max_total_value = np.ceil(max_total_value / 10.0) * 10
elif max_total_value <= 1000:
    max_total_value = np.ceil(max_total_value / 100.0) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set suitable colors and transparency
colors = ['#2B8CBE', '#FC4E2A', '#31A354', '#FDBB84', '#B3E2CD']
for i, area in enumerate(df.columns[1:]):
    ax.get_children()[i].set_facecolor(colors[i])
    ax.get_children()[i].set_alpha(0.8)

# set background grid lines
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.2)

# set legend and adjust position
leg = ax.legend(loc='upper left')
for legobj in leg.legendHandles:
    legobj.set_linewidth(2.0)
plt.setp(leg.get_texts(), color='black')

# add title and labels
ax.set_title('Student Enrollment Trends in Science and Engineering Fields', fontsize=14)
ax.set_xlabel('Area of Study', fontsize=12)
ax.set_ylabel('Number of Students', fontsize=12)

# resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_36.png', bbox_inches='tight')

# clear current image state
plt.clf()