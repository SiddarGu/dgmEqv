
import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))
labels = ['Football', 'Basketball', 'Baseball', 'Ice Hockey', 'Other Sports']
percentages = [40, 25, 15, 10, 10]
explode = (0.1, 0, 0, 0, 0) 
plt.pie(percentages, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 10, 'wrap': True, 'rotation': 45})
plt.title("Popular Sports in the USA, 2023")
plt.tight_layout()
plt.savefig("pie chart/png/39.png")
plt.clf()