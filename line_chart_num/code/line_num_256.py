
import matplotlib.pyplot as plt
import numpy as np

# Set data
age = ['18-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60']
salary = [45000, 65000, 82000, 95000, 105000, 115000, 108000, 100000]

# Create figure
fig = plt.figure(figsize=(15, 8))

# Plot line chart
plt.plot(age, salary, '--', color='blue', marker='o', label='Average Salary')

# Set label
plt.title('Average Salary of Employees by Age Group in 2021', fontsize=18)
plt.xlabel('Age', fontsize=16)
plt.ylabel('Average Salary (USD)', fontsize=16)

# Set xticks
plt.xticks(np.arange(len(age)), age, rotation=45, ha='right')

# Annotate
for i, j in zip(age, salary):
    plt.annotate(str(j), xy=(i, j), fontsize=14)

# Set legend
plt.legend(loc='upper left', fontsize=16)

# Set grid
plt.grid(linestyle='--', alpha=0.6)

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('line chart/png/12.png', dpi=200)

# Clear current image state
plt.clf()