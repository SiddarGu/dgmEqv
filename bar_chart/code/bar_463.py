
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(10, 6))

# Create subplot
ax = fig.add_subplot(111)

# Define data and labels
activities = ['Basketball', 'Soccer', 'Swimming', 'Running']
youth = [30, 40, 50, 25]
adults = [45, 50, 35, 35]
seniors = [20, 25, 30, 40]

# Create bars
ax.bar(activities, youth, label='Youth', width=0.3, bottom=0)
ax.bar(activities, adults, label='Adults', width=0.3, bottom=youth)
ax.bar(activities, seniors, label='Seniors', width=0.3, bottom=[i+j for i,j in zip(youth, adults)])

# Set title and labels
ax.set_title('Participation in sports activities by age group in 2021')
ax.set_xlabel('Activity')
ax.set_ylabel('Participation (%)')

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

# Set ticks
plt.xticks(rotation=45, ha='right', wrap=True)

# Resize image
plt.tight_layout()

# Save image
plt.savefig('bar chart/png/82.png', dpi=300)

# Clear current image state
plt.clf()