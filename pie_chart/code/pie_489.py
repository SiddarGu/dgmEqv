
import matplotlib.pyplot as plt 

labels = ['Bachelor\'s Degrees', 'Master\'s Degrees', 'Doctoral Degrees', 'Professional Degrees', 'Associate\'s Degrees']
sizes = [37, 30, 18, 10, 5]

plt.figure(figsize=(8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12})
plt.title('Degree Distribution of Higher Education in the US, 2023')
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/5.png')
plt.clf()