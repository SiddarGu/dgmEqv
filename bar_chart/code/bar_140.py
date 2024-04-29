
import matplotlib.pyplot as plt
import numpy as np

data = [['USA',200,4500],['UK',300,5000],['Germany',180,4000],['France',230,4700]]

Country = [x[0] for x in data]
Hospitals = [x[1] for x in data]
Doctors = [x[2] for x in data]

x = np.arange(len(Country))

fig, ax = plt.subplots(figsize=(10,7))

ax.bar(x-0.2, Hospitals, width=0.4, label='Hospitals', color='#FF9F33')
ax.bar(x+0.2, Doctors, width=0.4, label='Doctors', color='#6DABFF')

ax.set_xticks(x)
ax.set_xticklabels(Country, rotation=45, wrap=True)
ax.set_title('Number of hospitals and doctors in four countries in 2021')
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/264.png')
plt.clf()