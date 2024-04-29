
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Plotting data
Country = ['USA', 'UK', 'Germany', 'France']
Hospitals = [450, 370, 320, 400]
Clinics = [550, 580, 570, 650]
Doctors = [1000, 900, 850, 950]

ax.bar(Country, Hospitals, label='Hospitals', bottom=Clinics)
ax.bar(Country, Clinics, label='Clinics')
ax.bar(Country, Doctors, label='Doctors')

# Settings
ax.set_title('Number of healthcare facilities, clinics and doctors in four countries in 2021')
ax.set_ylabel('Number')
ax.grid(axis='y')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
fig.tight_layout()
ax.set_xticklabels(Country, rotation=45, wrap=True)

# Save figure
plt.savefig('bar chart/png/233.png')
plt.clf()