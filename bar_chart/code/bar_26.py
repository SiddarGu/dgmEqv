
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12, 6))
x = ['USA', 'UK', 'Germany', 'France']
width = 0.2
ax.bar(x, [150, 180, 170, 140], width=width, label='Movie Theaters')
ax.bar(x, [200, 230, 210, 190], width=width, bottom=[150, 180, 170, 140], label='Cinemas')
ax.bar(x, [300, 280, 250, 240], width=width, bottom=[350, 410, 380, 330], label='Concerts')
ax.set_title('Number of movie theaters, cinemas and concerts in four countries in 2021')
ax.set_xticks(x)
plt.xticks(rotation=30)
ax.legend(loc="best")
plt.tight_layout()
plt.savefig('bar chart/png/93.png')
plt.clf()