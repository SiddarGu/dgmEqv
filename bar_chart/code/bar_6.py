
import matplotlib.pyplot as plt
import numpy as np

data = [[50,100,50],[55,95,45],[60,85,60],[65,90,55]]
region = ['East','West','North','South']
hospitals = [50,55,60,65]
clinics = [100,95,85,90]
medical_centers = [50,45,60,55]

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(region, hospitals, label='Hospitals', bottom=clinics)
ax.bar(region, clinics, label='Clinics', bottom=medical_centers)
ax.bar(region, medical_centers, label='Medical Centers')
ax.set_title('Number of healthcare facilities in four regions in 2021')
ax.legend(loc='best')
plt.xticks(rotation=45, ha='right', wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/172.png')
plt.clf()