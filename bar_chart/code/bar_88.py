
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,6))
ax = plt.subplot()
ax.set_facecolor('#f7f7f7')
country = np.array(['USA', 'UK', 'Germany','France'])
num_schools = np.array([1000,1200,980,1150])
num_students = np.array([20000,25000,22000,23500])

ax.bar(country, num_schools, label='Schools', width=0.4, bottom=0, color='#6897bb')
ax.bar(country, num_students, label='Students', width=0.4, bottom=0, color='#fec615')

plt.title('Number of Schools and Students in four countries in 2021')
plt.xticks(country, rotation=45, ha='right')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/182.png')
plt.clf()