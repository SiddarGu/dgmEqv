
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Create figure 
fig = plt.figure(figsize=(12,7))

# Set x-axis
x = np.arange(2019,2023)

# Set y-axis
y1 = [60000, 65000, 70000, 75000]
y2 = [10, 15, 20, 25]
y3 = [2500, 3000, 3500, 4000]

# Draw line
plt.plot(x, y1, label="Average Salary(dollars)")
plt.plot(x, y2, label="Vacation Days")
plt.plot(x, y3, label="Employees")

# Set x-axis, y-axis label
plt.xlabel("Year")
plt.ylabel("Number")

# Set x-axis tick labels
plt.xticks(x)

# Set grid
plt.grid(True, linestyle='-.')

# Set title
plt.title("Employee Benefits and Salary Trends in a Large Company", fontsize = 16)

# Display legend
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', borderaxespad=0.)

# Label value of each data point directly on the figure
plt.annotate("60000", xy=(2019, 60000), xytext=(2019.1, 62500), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("65000", xy=(2020, 65000), xytext=(2020.1, 67500), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("70000", xy=(2021, 70000), xytext=(2021.1, 72500), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("75000", xy=(2022, 75000), xytext=(2022.1, 77500), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("10", xy=(2019, 10), xytext=(2018.9, 10.5), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("15", xy=(2020, 15), xytext=(2020, 15.5), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("20", xy=(2021, 20), xytext=(2021, 20.5), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("25", xy=(2022, 25), xytext=(2022, 25.5), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("2500", xy=(2019, 2500), xytext=(2018.9, 2750), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("3000", xy=(2020, 3000), xytext=(2020, 3250), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("3500", xy=(2021, 3500), xytext=(2021, 3750), fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("4000", xy=(2022, 4000), xytext=(2022, 4250), fontsize=10, arrowprops=dict(arrowstyle="->"))

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/113.png')

# Clear the current image state
plt.clf()