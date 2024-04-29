
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ["Personnel Training", "Employee Retention", "Talent Acquisition", "Workplace Safety", "Staff Engagement"]
data = [0.19, 0.25, 0.15, 0.22, 0.19]
line_labels = ["Category", "Ratio"]

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, aspect='equal')

# Create pie chart
ax.pie(data, startangle=90, counterclock=False, 
       colors=['#0084ff', '#a1e1f2', '#ffa600', '#f5b180', '#00c36b'])

# Create circle to turn pie chart into a ring chart
center_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(center_circle)

# Set title
ax.set_title("Employee Management Metrics - 2023", fontdict={'fontsize':20}, pad=20)

# Legend
ax.legend(data_labels, bbox_to_anchor=(1, 0.5), loc="center right")

# Automatically resize the image
fig.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_8.png')

# Clear the current image state
plt.clf()