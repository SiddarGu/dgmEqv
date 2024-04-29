
import matplotlib.pyplot as plt

data = [['USA',20000,30000],
        ['UK',25000,35000],
        ['Germany',22000,32000],
        ['France',21000,33000]]

x_pos = [i for i, _ in enumerate(data)]

plt.figure(figsize=(8,4))

plt.bar(x_pos, [i[1] for i in data], width=0.4, label='Criminal Cases')
plt.bar([i+0.4 for i in x_pos], [i[2] for i in data], width=0.4, label='Civil Cases')

plt.xticks([i+0.2 for i in x_pos], [i[0] for i in data], rotation=60, wrap=True)

plt.title('Number of criminal and civil cases in four countries in 2021')
plt.legend()

plt.tight_layout()
plt.savefig('bar chart/png/469.png')

plt.clf()