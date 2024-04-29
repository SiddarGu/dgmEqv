
import matplotlib.pyplot as plt
import matplotlib.patches as patches

data_labels = ['Cargo Delivery', 'Logistics Management', 'Fleet Management', 'Shipping Management']
data = [45, 30, 15, 10]
line_labels = ['Type', 'ratio']

# Create figure
fig, ax = plt.subplots(figsize=(12, 12))



# Plot the pie chart
ax.pie(data, labels=data_labels, 
       autopct='%1.1f%%', startangle=90, 
       counterclock=False, labeldistance=1.1,
       pctdistance=0.8)
# Create a circle in the center of the plot
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

# Add legend
ax.legend(data_labels, loc="best")

# Set title
plt.title('Transportation and Logistics Performance - 2023')

# Automatically adjust the layout
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_15.png')

# Clear current figure
plt.clf()