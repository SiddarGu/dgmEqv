
import matplotlib.pyplot as plt
import pandas as pd

data = {'Region': ['North', 'South', 'East', 'West'],
        'Hospitals': [100, 110, 120, 90],
        'Clinics': [200, 190, 180, 210],
        'Pharmacies': [150, 170, 190, 160]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(8,4))

ax.bar(df['Region'], df['Hospitals'], bottom=df['Clinics']+df['Pharmacies'], label='Hospitals')
ax.bar(df['Region'], df['Clinics'], bottom=df['Pharmacies'], label='Clinics')
ax.bar(df['Region'], df['Pharmacies'], label='Pharmacies')

ax.set_title('Number of healthcare facilities in four regions in 2021')
ax.set_xticks(df['Region'])
ax.legend(loc='upper left')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('bar chart/png/155.png', bbox_inches='tight')
plt.clf()