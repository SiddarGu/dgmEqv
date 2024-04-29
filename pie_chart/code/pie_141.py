
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Create figure
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)

# Data
Health_Factors = ['Exercise', 'Diet', 'Stress Management', 'Sleep', 'Genetics']
Percentage = [25, 25, 20, 15, 15]

# Plot pie chart
ax.pie(Percentage, labels=Health_Factors, autopct='%1.1f%%', 
        shadow=True, startangle=90, explode=(0, 0, 0.2, 0, 0))

# Title
ax.set_title('Impact of Health Factors on Well-Being, 2023', fontsize=20)

# Adjust the image
plt.tight_layout()
plt.xticks(rotation=45)

# Save the figure
plt.savefig('pie chart/png/480.png', bbox_inches='tight')

# Clear the current image state
plt.clf()