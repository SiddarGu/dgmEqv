
import matplotlib.pyplot as plt
import numpy as np

# Set data
country = ['USA', 'UK', 'Germany', 'France']
ave_education_level = [13, 14, 12, 14]
ave_education_expenditure = [6000, 8000, 7000, 9000]

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot() 
ax.bar(country, ave_education_level, bottom=ave_education_expenditure, label='Average Education Level')
ax.bar(country, ave_education_expenditure, label='Average Education Expenditure')

# Set legend
ax.legend(loc='best')

# Set title
ax.set_title('Average Education Level and Expenditure in Four Countries in 2021')

# Set xticks
plt.xticks(rotation=45, ha='right')

# Resize
plt.tight_layout()

# Save Figure
plt.savefig('bar chart/png/122.png')

# Clear image state
plt.clf()