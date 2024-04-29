
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10,5))

# Set labels
labels = ['USA', 'UK', 'Germany', 'France']

# Set data
Tax_Rate = [25, 20, 32, 27]
Minimum_Wage = [7.25, 8.72, 9.35, 10.15]
Voting_Age = [18, 16, 18, 18]

# Create bar chart
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

# Define bar commands
ax = plt.subplot()
ax.bar(x - width/2, Tax_Rate, width, label='Tax Rate', color='b')
ax.bar(x + width/2, Minimum_Wage, width, label='Minimum Wage', color='r')
ax.bar(x + width + width/2, Voting_Age, width, label='Voting Age', color='y')

# Set labels and title
ax.set_ylabel('Percentage/ Wage/ Age')
ax.set_title('Government policies in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(labels)

# Set legend
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/126.png')

# Clear current image state
plt.clf()