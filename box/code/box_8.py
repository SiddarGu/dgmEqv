
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
Home_Type = ["Entry-level","Experienced","Managerial","Senior Level","Executive"]
Min_Salary = [20000,45000,60000,80000,100000]
Q1_Salary = [40000,65000,87000,100000,150000]
Median_Salary = [60000,90000,120000,130000,200000]
Q3_Salary = [80000,115000,150000,170000,250000]
Max_Salary = [100000,150000,200000,220000,300000]
Outlier_Salary = [[], [200000], [10000], [250000], [310000]]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.set_title("Salary Distribution of Employees in Human Resources in 2021")
ax.boxplot(np.array([Min_Salary, Q1_Salary, Median_Salary, Q3_Salary, Max_Salary]), labels=Home_Type, showmeans=True)

# Plot the outliers
for x in range(len(Home_Type)):
    y = Outlier_Salary[x]
    if len(y) > 0:
        x_coords = np.repeat(x+1, len(y))
        ax.plot(x_coords, y, "bx")
ax.set_ylabel('Salary (USD)')
# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/box/png_val/box_8.png")

# Clear the current image state
plt.clf()