
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))

# Data to plot
labels = 'Music', 'Visual Arts', 'Theatre', 'Dance', 'Literature', 'Film'
sizes = [30, 25, 15, 15, 10, 5]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'pink']
explode = (0, 0, 0, 0, 0, 0.1)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Popular Art Forms in the United States, 2023')
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=90)

plt.savefig('pie chart/png/185.png')
plt.clf()