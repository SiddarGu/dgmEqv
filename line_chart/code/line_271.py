
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15, 8))
ax = plt.subplot()

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
aerodynamic_force = [100, 120, 140, 150, 190, 210, 220, 250]
wind_speed = [2.5, 3.2, 3.7, 4.0, 4.4, 4.7, 5.0, 5.3]

ax.plot(month, aerodynamic_force, label='Aerodynamic Force (N)', marker='o')
ax.plot(month, wind_speed, label='Wind Speed (m/s)', marker='o')

ax.set_title('Aerodynamic Force and Wind Speed in an Aircraft in Summer')
ax.set_xlabel('Month')
ax.set_ylabel('Force / Speed')
ax.grid(True)
ax.set_xticks(month)
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('line chart/png/194.png')
plt.clf()