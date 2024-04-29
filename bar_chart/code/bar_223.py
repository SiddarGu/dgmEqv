
import matplotlib.pyplot as plt
import numpy as np

labels = np.array(['North America', 'South America', 'Europe', 'Asia'])
x_pos = np.arange(len(labels))

Education_Spending = [100, 120, 140, 160]
Healthcare_Spending = [150, 170, 190, 210]
Transport_Spending = [80, 90, 100, 110]

fig, ax = plt.subplots(figsize=(8,4))

bar_width = 0.2
ax.bar(x_pos, Education_Spending, bar_width, label='Education Spending')
ax.bar(x_pos + bar_width, Healthcare_Spending, bar_width, label='Healthcare Spending')
ax.bar(x_pos + bar_width*2, Transport_Spending, bar_width, label='Transport Spending')

ax.set_xticks(x_pos + bar_width)
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_ylabel('Spending (million)')
ax.set_title('Government spending on education, healthcare, and transport in four regions in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)

plt.tight_layout()
plt.savefig('bar chart/png/15.png')
plt.clf()