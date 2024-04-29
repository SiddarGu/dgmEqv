
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))

data = [['USA', 25, 10], ['UK', 20, 12], ['Germany', 15, 15], ['France', 18, 14]]

Country = [item[0] for item in data]
High_School_Enrollment = [item[1] for item in data]
University_Enrollment = [item[2] for item in data]

ax.bar(Country, High_School_Enrollment, label='High School Enrollment (million)', bottom=University_Enrollment)
ax.bar(Country, University_Enrollment, label='University Enrollment (million)')

plt.legend(loc='upper left')
plt.title('High school and university enrollment in four countries in 2021')
plt.xticks(rotation=45, ha='right', wrap=True)
plt.tight_layout()

plt.savefig('bar chart/png/22.png')
plt.clf()