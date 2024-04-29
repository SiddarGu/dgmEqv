
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
treatment_types = ('Prescription Drugs', 'Surgery', 'Physical Therapy', 'Alternative Medicine', 'Therapies', 'Lifestyle Changes')
percentages = (20,30,20,10,10,10)
ax.pie(percentages, labels=treatment_types, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 11})
ax.axis('equal')
plt.title('Healthcare Treatment Distribution in the USA,2023')
plt.tight_layout()
plt.savefig('pie chart/png/214.png', bbox_inches='tight')
plt.clf()