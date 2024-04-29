
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

country = ['USA','UK','Germany','France']
enrolled = [2.5,1.8,1.2,1.9]
graduates = [0.5,0.4,0.3,0.7]

ax.bar(country, enrolled, width=0.4, label='Students Enrolled', color='blue')
ax.bar(country, graduates, width=0.4, bottom=enrolled, label='Graduates', color='orange')
ax.set_title('Student enrollment and graduation rates in four countries in 2021', fontsize=18)
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('Students', fontsize=14)
ax.set_xticklabels(country, rotation=45, ha='right', fontsize=12)
ax.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.savefig('bar chart/png/267.png')
plt.clf()