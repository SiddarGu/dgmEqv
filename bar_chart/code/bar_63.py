
import matplotlib.pyplot as plt
import numpy as np

country = ['USA', 'UK', 'Germany', 'France']
average_score = [80.2, 65.3, 70.1, 75.3]
number_of_students = [20000, 18000, 19000, 21000]

plt.figure(figsize=(8, 8))

ax = plt.subplot()
ax.bar(country, average_score, width=0.4, bottom=number_of_students, label='Average Score')
ax.bar(country, number_of_students, width=0.4, label='Number of Students')

plt.xticks(country, rotation=45, wrap=True)
plt.title('Average score and number of students in four countries in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/8.png')

plt.clf()