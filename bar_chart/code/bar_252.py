
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()

ax.bar(x=['USA','UK','Germany','France'], height=[10000, 8000, 9000, 7000], label='Number of Schools', color='#3399ff', width=0.5)
ax.bar(x=['USA','UK','Germany','France'], height=[6000000, 4000000, 5000000, 3000000], label='Number of Students', color='#ff9900', bottom=[10000, 8000, 9000, 7000], width=0.5)

ax.set_title('Number of Schools and Students in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')

ax.legend(loc='upper right')

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar chart/png/482.png')
plt.clf()