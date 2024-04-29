
import matplotlib.pyplot as plt
import numpy as np 

# Create data
Country = ['USA', 'UK', 'Germany', 'France']
Employees = [10, 12, 11, 9]
Hours = [120, 130, 140, 150]

# Create figure
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot()

# Plot bars
ax.bar(Country, Employees, bottom=0, color='xkcd:azure', label='Employees')
ax.bar(Country, Hours, bottom=Employees, color='xkcd:light orange', label='Hours')

# Set title and labels
ax.set_title('Number of employees and total hours worked in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number of Employees and Hours')

# Add legend
ax.legend(loc='upper right')

# Automatically resize the image
plt.tight_layout()

# Annotate
for i in range(len(Country)):
    ax.annotate(Employees[i], xy=(Country[i],Employees[i]/2))
    ax.annotate(Hours[i], xy=(Country[i],Employees[i]+Hours[i]/2))

# Xticks
plt.xticks(Country)

# Save the figure
plt.savefig('Bar Chart/png/419.png')

# Clear the current image state
plt.clf()