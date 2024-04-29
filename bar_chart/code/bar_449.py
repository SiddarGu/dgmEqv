
import matplotlib.pyplot as plt

data = [['USA', 5, 7, 8], 
        ['UK', 6, 7, 9], 
        ['Germany', 7, 6, 8], 
        ['France', 8, 7, 9]]

labels = [item[0] for item in data]
Economics = [item[1] for item in data]
Politics = [item[2] for item in data]
Education = [item[3] for item in data]

x_pos = [i for i, _ in enumerate(labels)]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1, 1, 1)
ax.bar(x_pos, Economics, width=0.2, label='Economics', color='red')
ax.bar([p + 0.2 for p in x_pos], Politics, width=0.2, label='Politics', color='green')
ax.bar([p + 0.4 for p in x_pos], Education, width=0.2, label='Education', color='blue')

plt.xticks([p + 0.1 for p in x_pos], labels, rotation='vertical')
plt.title("Social sciences and humanities index of four countries in 2021")
plt.xlabel("Country")
plt.ylabel("Index")
plt.legend(loc='best')

plt.tight_layout()

plt.savefig('bar chart/png/149.png')
plt.clf()