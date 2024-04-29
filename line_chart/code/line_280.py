
import matplotlib.pyplot as plt
import numpy as np

x = np.array([20, 30, 40, 50, 60])
y1 = np.array([23, 25, 27, 29, 31])
y2 = np.array([100, 120, 140, 160, 180])

plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.plot(x, y1, '--b', label='Average BMI')
ax.plot(x, y2, '-r', label='Average Blood Sugar')
ax.set_xticks(x)
ax.set_title('Average BMI and Blood Sugar Levels of Different Age Groups in the United States')
plt.xlabel('Age')
plt.ylabel('Value')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/507.png')
plt.clf()