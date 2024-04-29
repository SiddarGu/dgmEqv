
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot()
ax.set_xlabel('Country')
ax.set_ylabel('GDP (trillion dollars)')
ax.set_title('Gross Domestic Product of Major Countries in 2020')

data = [['USA', 20], ['China', 14], ['India', 7], ['Germany', 3],
        ['Japan', 3], ['France', 2], ['UK', 2], ['Italy', 1], ['Canada', 1]]

x = [point[0] for point in data]
y = [point[1] for point in data]

ax.plot(x, y, marker='o', linestyle='--', color='orange')
ax.set_xticklabels(x, rotation=45, ha="right", wrap=True)

for i, j in zip(x, y):
    ax.annotate(str(j), xy=(i, j))

plt.tight_layout()
plt.savefig('line chart/png/97.png')
plt.clf()