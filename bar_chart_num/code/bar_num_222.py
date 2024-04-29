
import matplotlib.pyplot as plt

#Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Data
region = ['East', 'West', 'North', 'South']
schools = [100, 90, 110, 95]
hospitals = [20, 25, 30, 35]
police = [15, 17, 20, 22]

# Plot the data
ax.bar(region, schools, label='Schools')
ax.bar(region, hospitals, bottom=schools, label='Hospitals')
ax.bar(region, police, bottom=[schools[i] + hospitals[i] for i in range(len(schools))], label='Police Stations')

# Add legend
ax.legend(loc='upper left')

# Title
plt.title('Number of Schools, Hospitals and Police Stations in four regions in 2021')

# Annotate values
for i in range(len(region)):
    ax.text(x=i, y=schools[i]+hospitals[i]+police[i]+2, s=schools[i]+hospitals[i]+police[i], ha='center', va='bottom')

# Automatically resize
plt.tight_layout()

# xticks
plt.xticks(rotation=45)

# Save the figure
plt.savefig('Bar Chart/png/499.png')

# Clear the current image state
plt.clf()