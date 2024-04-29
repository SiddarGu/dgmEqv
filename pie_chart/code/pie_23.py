
import matplotlib.pyplot as plt
import numpy as np

age = np.array(['0-14 years', '15-24 years', '25-54 years', '55-64 years', '65 years and over'])
population = np.array([23, 14, 43, 12, 8])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

#pie chart
ax.pie(population, labels=age, autopct='%.2f%%', startangle=90, explode=(0.05, 0, 0, 0, 0))

#legend
ax.legend(loc='best', labels=age)

#title
ax.set_title('Population Distribution by Age Group in the USA, 2023')

#tight layout
plt.tight_layout()

#save image
plt.savefig('pie chart/png/11.png')

#clear
plt.clf()