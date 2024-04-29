
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15,8))

ax = fig.add_subplot(111)

x = np.array(['18-25', '25-35', '35-45', '45-55', '55-65'])
y1 = np.array([25, 27, 30, 32, 34])
y2 = np.array([60, 70, 75, 80, 85])
y3 = np.array([170, 175, 180, 185, 190])

ax.plot(x, y1, color='red', label='Average BMI')
ax.plot(x, y2, color='blue', label='Average Weight (kg)')
ax.plot(x, y3, color='green', label='Average Height (cm)')

ax.set_xlabel('Age')
ax.set_ylabel('Measurements')
ax.set_title('Average Body Measurements of Different Age Groups', fontsize = 20)
ax.legend(loc='best', prop={'size': 15})
ax.grid(True, linestyle='--', color='gray', alpha=0.5)
plt.xticks(x, fontsize=15)
plt.yticks(fontsize=15)
plt.tight_layout()

plt.savefig('line chart/png/130.png')
plt.clf()