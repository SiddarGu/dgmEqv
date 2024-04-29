
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# Plot data
country = ['USA','UK','Germany','France']
schooling_age = [17,16,16,16]
years_of_education = [12,13,12,12]

ax.bar(country, schooling_age, bottom=years_of_education, color='#008080', label='Schooling Age')
ax.bar(country, years_of_education, color='#e6e600', label='Years of Education')

# Set fontsize
plt.rcParams.update({'font.size': 12})

# Set title
plt.title('Average Schooling Age and Years of Education in four countries in 2021')

# Set legend
ax.legend()

# Set xticks
plt.xticks(np.arange(4),country)

# Adjust figure
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/473.png')

# Clear current image state
plt.clf()