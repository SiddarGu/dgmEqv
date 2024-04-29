
import matplotlib.pyplot as plt

# Create figure and set title
fig = plt.figure(figsize=(8, 8))
plt.title('Distribution of Science and Engineering Fields in the USA, 2023')

# Define the data
fields = ['Physical Sciences', 'Engineering', 'Mathematics', 'Computer Science', 'Information Science', 'Biology', 'Chemistry']
percentage = [18, 30, 12, 20, 10, 5, 5]

# Plot the data
plt.pie(percentage, labels=fields, autopct='%1.1f%%', textprops={'fontsize': 14, 'wrap': True}, labeldistance=1.05, rotatelabels=True)
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/514.png')

# Clear the current image state
plt.clf()