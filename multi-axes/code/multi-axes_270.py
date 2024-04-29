

import numpy as np
import matplotlib.pyplot as plt 

# transform the data
data_labels = ["Number of Employees", "Average Salary (Dollars)", "Average Working Hours (Hours)"]
line_labels = ["Recruiting", "Training", "Performance Management", "Diversity and Inclusion",
               "Employee Engagement", "Benefits Administration", "Payroll", "Compliance", "Career Development"]
data = np.array([[750, 18500, 37],
                 [560, 13400, 40],
                 [480, 14700, 38],
                 [200, 18000, 35],
                 [400, 17200, 41],
                 [100, 13000, 39],
                 [650, 15000, 37],
                 [300, 19000, 33],
                 [450, 14300, 42]])

# plot the data
plt.figure(figsize=(15, 10))
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:, 0], color="red")
ax1.set_ylabel(data_labels[0], color="red")
ax1.set_xlabel("Category")
ax1.tick_params(axis="y", colors="red")

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color="blue")
ax2.set_ylabel(data_labels[1], color="blue")
ax2.tick_params(axis="y", colors="blue")

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color="green")
ax3.spines["right"].set_position(("axes", 1.1))
ax3.set_ylabel(data_labels[2], color="green")
ax3.tick_params(axis="y", colors="green")

plt.title("Human Resources and Employee Management Overview: Employee Number, Average Salary, and Working Hours", fontsize=16)
ax1.xaxis.set_tick_params(rotation=45)
plt.autoscale(enable=True, axis='both', tight=True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/20_2023122261325.png")
plt.clf()