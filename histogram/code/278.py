import matplotlib.pyplot as plt

# Data
data_labels = ['Underweight (<18.5)', 'Normal weight (18.5-24.9)', 'Overweight (25-29.9)',
               'Obesity (30-34.9)', 'Severe Obesity (35-39.9)', 'Morbid Obesity (>=40)']
data = [12, 35, 27, 16, 7, 3]

# Creating figure and adding subplots
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Setting title of the figure
ax.set_title('Prevalence of BMI Categories in the Adult Population')

# Plotting the histogram
ax.bar(data_labels, data, color=plt.cm.Paired.colors)

# Adding background grids
ax.grid(axis='y', linestyle='--')

# Rotate the x labels if they are too long
plt.xticks(rotation=30, ha='right')

# Adjust layout to make room for the rotated x labels
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/628.png')

# Show plot (optional, remove the comment if you want to see the plot in an interactive session)
# plt.show()

# Clear the current figure's state to avoid interference with other plots
plt.clf()
