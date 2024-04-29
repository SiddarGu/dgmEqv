
import matplotlib.pyplot as plt

data = {'Country': ['USA', 'UK', 'Germany', 'France'], 
        'Social Studies': [10, 11, 9, 8], 
        'Humanities': [12, 13, 14, 15]}

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

x = data['Country']
y1 = data['Social Studies']
y2 = data['Humanities']

ax.bar(x, y1, label='Social Studies', width=0.4)
ax.bar(x, y2, label='Humanities', bottom=y1, width=0.4)

ax.set_title('Weekly hours spent on social studies and humanities in four countries in 2021')
ax.set_xticks(x)
ax.set_xlabel('Country')
ax.set_ylabel('Hours/Week')
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig('bar chart/png/314.png')
plt.clf()