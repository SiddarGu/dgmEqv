
import matplotlib.pyplot as plt
import numpy as np

# Create figure before plotting
fig = plt.figure(figsize=(10, 6))

# Pie chart
employee_type = ["Full-time", "Part-time", "Contractor", "Intern", "Volunteer"]
percentage = [45, 30, 10, 10, 5]

# Automatically resize the image by tight_layout()
plt.tight_layout()

# You must use xticks to prevent interpolation
plt.xticks(rotation=90)

# Set title
plt.title("Distribution of Employee Types in the Workforce, 2023")

# Plot the data with the type of pie chart
plt.pie(percentage, labels=employee_type, autopct='%1.0f%%', pctdistance=0.7)

# Saving the figure
plt.savefig('pie chart/png/497.png')

# Clear the current image state at the end of the code
plt.clf()