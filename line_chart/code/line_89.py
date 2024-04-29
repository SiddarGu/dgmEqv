
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(20,10))
ax = plt.subplot()

ax.set_title('Average scores for students in grades 6 to 12')

x_data = np.array(['6th', '7th', '8th', '9th', '10th', '11th', '12th'])
y_data = np.array([85, 87, 90, 92, 95, 93, 90])

ax.plot(x_data, y_data, color='#2E9AFE', linestyle='solid', marker='o', markersize=6, markerfacecolor='#2E9AFE')
ax.set_xticks(x_data)
plt.xticks(rotation=45, fontsize=12, wrap=True)
plt.tight_layout()
plt.savefig('line chart/png/22.png')
plt.clf()