
import matplotlib.pyplot as plt
import numpy as np

x_data = np.array(['January','February','March','April','May','June','July','August','September','October','November','December'])
y1_data = np.array([4.2,4.7,5.3,6.2,7.1,7.4,6.5,5.3,4.2,3.8,4.3,4.8])
y2_data = np.array([400,355,350,280,225,200,150,90,125,155,250,300])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.set_title('Wind Speed and Solar Radiation in a Coastal Town in 2021', fontsize=15)

ax.plot(x_data, y1_data, label='Wind Speed (m/s)', marker='o')
ax.plot(x_data, y2_data, label='Solar Radiation (W/m2)', marker='o')

ax.set_xlabel('Month', fontsize=13)
ax.set_xticks(x_data)

plt.legend(loc='upper right')
plt.grid()
plt.tight_layout()

plt.savefig('line chart/png/452.png')

plt.clf()