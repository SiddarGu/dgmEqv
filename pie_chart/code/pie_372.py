
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
labels = ['Excercise', 'Eating Healthy', 'Mental Health', 'Sleep', 'Prevention']
sizes = [25, 30, 15, 15, 15]
plt.title('Distribution of Healthy Habits in the USA, 2023')
plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'rotation':35, 'wrap':True})
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/70.png')
plt.clf()