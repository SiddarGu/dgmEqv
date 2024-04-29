
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(12, 6)) 

# Data
countries = ['USA', 'UK', 'Germany', 'France']
education = [200, 250, 180, 230]
healthcare = [250, 300, 270, 290]
environment = [80, 90, 75, 100]

# Plot
ax = fig.add_subplot(111)
ax.bar(countries, education, label='Education Funding', bottom=0, color='#0f8dc7')
ax.bar(countries, healthcare, label='Healthcare Funding', bottom=education, color='#ec0f82')
ax.bar(countries, environment, label='Environmental Funding', bottom=[education[i]+healthcare[i] for i in range(len(countries))], color='#4ab24c')

# Title, labels and legend
ax.set_title('Public funding in three categories across four countries in 2021', fontsize=14)
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('Funding (billion)', fontsize=14)
ax.legend(loc='upper left')

# Modify x-axis
plt.xticks(rotation=90)

# Adjust figure size
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/123.png')

# Clear current image state
plt.clf()