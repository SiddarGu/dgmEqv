

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,6))
labels = ['Primary Care', 'Specialty Care', 'Hospital Care', 'Mental Health', 'Telemedicine']
sizes = [25, 40, 15, 10, 10]
explode = [0, 0, 0, 0.1, 0]

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Healthcare Services Distribution in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/262.png')
plt.clf()