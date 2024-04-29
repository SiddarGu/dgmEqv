
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Label setting
country = ['USA', 'Canada', 'Mexico', 'Brazil']
x = np.arange(len(country))
ax.set_xticks(x)
ax.set_xticklabels(country, rotation=45, ha='right', wrap=True)

# Plotting
ax.plot(x, [1000, 1200, 800, 1500], label='Drug A', marker='o', color='green')
ax.plot(x, [800, 900, 1100, 1200], label='Drug B', marker='o', color='blue')
ax.plot(x, [1200, 1100, 1300, 1400], label='Drug C', marker='o', color='red')

# Setting
ax.set_title('Number of Patients Treated with Drugs A, B and C in North American Countries in 2021')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/278.png')
plt.clf()