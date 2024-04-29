
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,7))

# Create data
Sources = ['Solar','Wind','Hydro','Nuclear','Other']
Percentage = [30,35,20,10,5]

# Plot
plt.pie(Percentage, labels=Sources, autopct='%1.1f%%', shadow=True, startangle=90)

# Legend
plt.legend(bbox_to_anchor=(1,1), loc='upper right', labelspacing=1.5, fontsize=10)

# Title
plt.title('Distribution of Energy Sources in the USA in 2023', fontsize=14, pad=12)

# Adjust parameters
plt.tight_layout()

# Save image
plt.savefig('pie chart/png/192.png')

# Clear image state
plt.clf()