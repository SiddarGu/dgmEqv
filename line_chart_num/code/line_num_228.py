
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.size'] = 10
plt.rcParams['axes.grid'] = True

# Create data
Year = np.array([2017,2018,2019,2020,2021])
Attendance = np.array([20,25,30,35,40])
Revenue = np.array([1.2,1.5,1.7,2.2,2.5])

# Create figure
plt.figure()
ax = plt.subplot()

# Plot line chart
line_chart_attendance = ax.plot(Year, Attendance, label='Attendance(millions)', color='#1f77b4')
line_chart_Revenue = ax.plot(Year, Revenue, label='Revenue(billion dollars)', color='#ff7f0e')
ax.set_xticks(Year)

# Set title and labels
ax.set_title('Rise of Attendance and Revenue in Sports Events from 2017 to 2021')
ax.set_xlabel('Year')
ax.set_ylabel('Attendance and Revenue (in millions)')

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)

# Add annotations
for x, y in zip(Year, Attendance):
    label = "{:.2f}".format(y)
    ax.annotate(label,
                (x, y),
                textcoords="offset points",
                xytext=(0, 10),
                ha='center')

for x, y in zip(Year, Revenue):
    label = "{:.2f}".format(y)
    ax.annotate(label,
                (x, y),
                textcoords="offset points",
                xytext=(0, 10),
                ha='center')

# Automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/433.png', bbox_inches='tight')

# Clear the current image state
plt.clf()