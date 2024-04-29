
import numpy as np
import matplotlib.pyplot as plt

# Set the font
plt.rcParams['font.family'] = 'sans-serif'

# Set the data
region = ['North America', 'South America', 'Europe', 'Africa']
hospitals = [50, 60, 70, 40]
doctors = [1000, 1200, 1400, 900]
patients = [20000, 25000, 30000, 20000]

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Plot stacked bar chart
ax.bar(region, hospitals, label='Hospitals', color='red')
ax.bar(region, doctors, bottom=hospitals, label='Doctors', color='blue')
ax.bar(region, patients, bottom=np.array(hospitals) + np.array(doctors), label='Patients', color='green')

# Add title and legend
ax.set_title('Number of hospitals, doctors and patients in four regions in 2021')
ax.legend(loc='best')

# Set axis labels
ax.set_xlabel('Region')
ax.set_ylabel('Number')

# Adjust the spacing
plt.tight_layout()

# Annotate values
for i, v in enumerate(hospitals):
    ax.text(i-0.2, v/2, str(v), color='white', fontweight='bold', fontsize=10)
for i, v in enumerate(doctors):
    ax.text(i-0.2, hospitals[i] + v/2, str(v), color='white', fontweight='bold', fontsize=10)
for i, v in enumerate(patients):
    ax.text(i-0.2, hospitals[i] + doctors[i] + v/2, str(v), color='white', fontweight='bold', fontsize=10)

# Save the figure
plt.savefig('Bar Chart/png/502.png')

# Clear the current image state
plt.clf()